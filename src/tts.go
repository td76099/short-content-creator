package main

import (
	"context"
	"fmt"
	"log"
	"io/ioutil"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/polly"
)

func generateAudio(ctx context.Context, voiceName string, languageCode string, textFile string) *polly.SynthesizeSpeechOutput {
	// Create a session with AWS Polly
	sess, err := session.NewSession(&aws.Config{
		Region: aws.String("us-east-1")},
	)
	if err != nil {
		log.Fatalf("Failed to create session: %v", err)
	}

	// Create Polly client
	svc := polly.New(sess)

	// The text to synthesize.
	textRaw, err := ioutil.ReadFile(textFile)
	text := string(textRaw)
	fmt.Println(text)

	// Perform the text-to-speech request
	input := &polly.SynthesizeSpeechInput{
		OutputFormat: aws.String("mp3"),
		Text:         aws.String(text),
		VoiceId:      aws.String(voiceName),
		LanguageCode: aws.String(languageCode),
	}

	resp, err := svc.SynthesizeSpeech(input)
	if err != nil {
		log.Fatalf("Failed to synthesize speech: %v", err)
	}

	return resp
}

func writeAudio(resp *polly.SynthesizeSpeechOutput, outputFile string){
	// Save the audio to a file
	defer resp.AudioStream.Close()
	audioBytes, err := ioutil.ReadAll(resp.AudioStream)
	if err != nil {
		log.Fatalf("Failed to read audio stream: %v", err)
	}

	err = ioutil.WriteFile(outputFile, audioBytes, 0644)
	if err != nil {
		log.Fatalf("Failed to write audio file: %v", err)
	}
}

func CreateTTS(voice string, languageCode string, textFile string, outputFile string){
	ctx := context.Background()
	resp := generateAudio(ctx, voice, languageCode, textFile)
	writeAudio(resp, outputFile)
}
