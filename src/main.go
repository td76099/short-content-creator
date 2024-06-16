package main

// import (
// 	"context"
// 	"fmt"
// 	"io/ioutil"
// 	"log"
// 	"os/exec"

// 	texttospeech "cloud.google.com/go/texttospeech/apiv1"
// 	texttospeechpb "google.golang.org/genproto/googleapis/cloud/texttospeech/v1"
// )

import (
	"fmt"
	"log"
	"math/rand"
	"os/exec"
	// "io/ioutil"
	"os"
	"time"
	"github.com/faiface/beep/mp3"
	
)

func main() {
	// token, err := getOAuthToken()
	// if err != nil {
	// 	fmt.Println("Error getting OAuth token:", err)
	// 	return
	// }
	// post, err := getTopPosts(token, "AmItheAsshole")
	// if err != nil {
	// 	fmt.Println("Error getting top posts:", err)
	// 	return
	// }

	// fmt.Printf("Title: %s\nURL: %s\nContent: %s\n\n", post.Title, post.URL, post.SelfText)
	// ioutil.WriteFile("output.txt", []byte(post.SelfText), 0644)
	// ctx := context.Background()

	// // Creates a client.
	// client, err := texttospeech.NewClient(ctx)
	// if err != nil {
	// 	log.Fatalf("Failed to create client: %v", err)
	// }

	// // The text to synthesize.
	// textRaw, err := ioutil.ReadFile("output.txt")
	// text := string(textRaw)
	// fmt.Println(text)

	// // Build the voice request, select the language code ("en-US") and the SSML voice gender.
	// voice := &texttospeechpb.VoiceSelectionParams{
	// 	LanguageCode: "en-US",
	// 	Name:         "en-US-Standard-H", // Change this to a standard voice if needed, e.g., "en-US-Standard-D"
	// }

	// // Select the type of audio file you want returned.
	// audioConfig := &texttospeechpb.AudioConfig{
	// 	AudioEncoding: texttospeechpb.AudioEncoding_MP3,
	// }

	// // Perform the text-to-speech request on the text input with the selected voice parameters and audio file type.
	// req := &texttospeechpb.SynthesizeSpeechRequest{
	// 	Input: &texttospeechpb.SynthesisInput{
	// 		InputSource: &texttospeechpb.SynthesisInput_Text{Text: text},
	// 	},
	// 	Voice:       voice,
	// 	AudioConfig: audioConfig,
	// }

	// resp, err := client.SynthesizeSpeech(ctx, req)
	// if err != nil {
	// 	log.Fatalf("Failed to synthesize speech: %v", err)
	// }

	// // Save the audio to a file.
	// err = ioutil.WriteFile("output.mp3", resp.AudioContent, 0644)
	// if err != nil {
	// 	log.Fatalf("Failed to write audio file: %v", err)
	// }

	// fmt.Println("Audio content written to file: output.mp3")
	// fmt.Println("we go next")
	// cmdResult := exec.Command("docker", "run", "--rm", "-v", "/mnt/g/Downloads3/short-content-creator:/tmp", "--entrypoint", "python", "lowerquality/gentle", "/gentle/align.py", "/tmp/output.mp3", "/tmp/output.txt")
	// out, err := cmdResult.Output()
    // if err != nil {
    //     fmt.Println(err.Error())
    //     return
    // }

    // // Print the output
    // fmt.Println(string(out))

	rand.Seed(time.Now().UnixNano())

	// File paths
	mp4File := "videos/background/mobile_gameplay_1.mp4"
	mp3File := "output.mp3"
	srtFile := "output.srt"
	outputFile := "output.mp4"
	fontName := "ComicSansMS"

	f, err := os.Open(mp3File)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	streamer, format, err := mp3.Decode(f)
	length := streamer.Len()
	audioLength := int(format.SampleRate.D(length)/time.Second)
	videoLength := 3600
	// Generate a random start time such that the video segment will fit within the video length
	startTime := rand.Intn(videoLength - audioLength)

	fmt.Printf("Random start time: %d seconds\n", startTime)

	// Extract the random segment from the MP4 file without audio
	extractSegmentCmd := exec.Command("ffmpeg", "-ss", fmt.Sprintf("%d", startTime), "-i", mp4File, "-t", fmt.Sprintf("%d", audioLength), "-an", "-vf", "crop=in_h*9/16:in_h", "-map", "0:v", "temp_video.mp4")
	err = extractSegmentCmd.Run()
	if err != nil {
		log.Fatalf("Failed to extract video segment: %v", err)
	}

	os.Setenv("FC_CONFIG_DIR", "/usr/share/fonts")
	os.Setenv("FONTCONFIG_PATH", "/usr/share/fonts")
	combineCmd := exec.Command("ffmpeg", "-i", "temp_video.mp4", "-i", mp3File, "-vf", "subtitles="+srtFile+":force_style='Outline=1,OutlineColour=&H000000&,FontName="+fontName+",FontSize=11,Alignment=10'", "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k", "-shortest", outputFile)
	err = combineCmd.Run()
	if err != nil {
		log.Fatalf("Failed to combine files: %v", err)
	}
	fmt.Printf("Output file created: %s\n", outputFile)
}
