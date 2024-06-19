package main

import (
	"context"
	"fmt"
	"log"
	"io/ioutil"

	texttospeech "cloud.google.com/go/texttospeech/apiv1"
	texttospeechpb "google.golang.org/genproto/googleapis/cloud/texttospeech/v1"
)

func generateAudio(ctx context.Context, voiceName string, textFile string) *texttospeechpb.SynthesizeSpeechResponse {
	client, err := texttospeech.NewClient(ctx)
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	// Select the type of audio file you want returned.
	audioConfig := &texttospeechpb.AudioConfig{
		AudioEncoding: texttospeechpb.AudioEncoding_MP3,
	}

	// Build the voice request, select the language code ("en-US") and the SSML voice gender.
	voice := &texttospeechpb.VoiceSelectionParams{
		LanguageCode: "en-US",
		Name:         voiceName, // Change this to a standard voice if needed, e.g., "en-US-Standard-D"
	}

	// The text to synthesize.
	textRaw, err := ioutil.ReadFile(textFile)
	text := string(textRaw)
	fmt.Println(text)

	// Perform the text-to-speech request on the text input with the selected voice parameters and audio file type.
	req := &texttospeechpb.SynthesizeSpeechRequest{
		Input: &texttospeechpb.SynthesisInput{
			InputSource: &texttospeechpb.SynthesisInput_Text{Text: text},
		},
		Voice:       voice,
		AudioConfig: audioConfig,
	}

	resp, err := client.SynthesizeSpeech(ctx, req)
	if err != nil {
		log.Fatalf("Failed to synthesize speech: %v", err)
	}

	return resp
}

func writeAudio(resp *texttospeechpb.SynthesizeSpeechResponse, outputFile string){
	// Save the audio to a file.
	err := ioutil.WriteFile(outputFile, resp.AudioContent, 0644)
	if err != nil {
		log.Fatalf("Failed to write audio file: %v", err)
	}
}

func CreateTTS(voice string, textFile string, outputFile string){
	ctx := context.Background()
	resp := generateAudio(ctx, voice, textFile)
	writeAudio(resp, outputFile)
}
