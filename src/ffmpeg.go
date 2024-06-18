package main

import (
	"fmt"
	"log"
	"math/rand"
	"os/exec"
	"os"
	"time"
	"path/filepath"
	"github.com/faiface/beep/mp3"
)

func getAudioLength(mp3File string) int {
	rand.Seed(time.Now().UnixNano())

	f, err := os.Open(mp3File)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	
	streamer, format, err := mp3.Decode(f)
	length := streamer.Len()
	audioLength := int(format.SampleRate.D(length)/time.Second) + 1
	
	return audioLength
}

func createBaseVideo(audioLength int, mp4File string) {
	videoLength := 3600
	// Generate a random start time such that the video segment will fit within the video length
	startTime := rand.Intn(videoLength - audioLength)
	
	fmt.Printf("Random start time: %d seconds\n", startTime)
	
	// Extract the random segment from the MP4 file without audio
	extractSegmentCmd := exec.Command("ffmpeg", "-ss", fmt.Sprintf("%d", startTime), "-i", mp4File, "-t", fmt.Sprintf("%d", audioLength), "-an", "-vf", "crop=in_h*9/16:in_h", "-map", "0:v", "temp_video.mp4")
	err := extractSegmentCmd.Run()
	if err != nil {
		log.Fatalf("Failed to extract video segment: %v", err)
	}
}

func createFinalVideo(fontDir string, fontName string, mp3File string, srtFile string, outputFile string) {
	os.Setenv("FC_CONFIG_DIR", fontDir)
	os.Setenv("FONTCONFIG_PATH", fontDir)
	
	outputPath := filepath.Dir(outputFile)
	if err := os.MkdirAll(outputPath, os.ModePerm); err != nil {
		fmt.Printf("Error creating directories: %v\n", err)
		return
	}

	combineCmd := exec.Command("ffmpeg", "-i", "temp_video.mp4", "-i", mp3File, "-vf", "subtitles="+srtFile+":force_style='Outline=1,OutlineColour=&H000000&,FontName="+fontName+",FontSize=11,Alignment=10'", "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k", "-shortest", outputFile)
	err := combineCmd.Run()
	if err != nil {
		log.Fatalf("Failed to combine files: %v", err)
	}
	fmt.Printf("Output file created: %s\n", outputFile)
}

func CreateVideo(fontDir string, fontName string, backgroundVideo string, subredditName string, postID string) {
	// File paths
	mp3File := "output.mp3"
	srtFile := "output.srt"
	outputFile := "output/"+subredditName+"/"+postID+".mp4"
	if (fontName == "") {
		fontName = "ComicSansMS"
	}

	audioLength := getAudioLength(mp3File)
	createBaseVideo(audioLength, backgroundVideo)
	createFinalVideo(fontDir, fontName, mp3File, srtFile, outputFile)
}