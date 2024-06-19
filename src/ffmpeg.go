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

func GetAudioLength(mp3File string) int {
	rand.Seed(time.Now().UnixNano())

	f, err := os.Open(mp3File)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	
	streamer, format, err := mp3.Decode(f)
	length := streamer.Len()
	audioLength := int(format.SampleRate.D(length)/time.Second)
	
	return audioLength
}

func createBaseVideo(audioLength int, titleAudioLength int, mp4File string, titleMP3 string, titleScreenshotName string) {
	videoLength := 3600
	// Generate a random start time such that the video segment will fit within the video length
	startTime := rand.Intn(videoLength - audioLength)
	
	fmt.Printf("Random start time: %d seconds\n", startTime)
	
	// Extract the random segment from the MP4 file without audio
	extractSegmentCmd := exec.Command("ffmpeg", "-ss", fmt.Sprintf("%d", startTime), "-i", mp4File, "-t", fmt.Sprintf("%d", audioLength), "-an", "-vf", "crop=in_h*9/16:in_h", "-map", "0:v", "temp_background.mp4")
	err := extractSegmentCmd.Run()
	if err != nil {
		log.Fatalf("Failed to extract video segment: %v", err)
	}

	// Overlay title screenshot and play title MP3 on the background video
	overlayTitleCmd := exec.Command("ffmpeg",
		"-i", "temp_background.mp4",
		"-i", titleScreenshotName,
		"-i", titleMP3,
		"-filter_complex", fmt.Sprintf("[1:v]scale=iw*0.55:ih*0.55[overlay];[0:v][overlay]overlay=(W-w)/2:(H-h)/2:enable='between(t,0,%d)'[v];[2:a]adelay=0|0[a1]", titleAudioLength),
		"-map", "[v]",
		"-map", "[a1]",
		"-c:v", "libx264",
		"-c:a", "aac",
		"temp_video.mp4")
    err = overlayTitleCmd.Run()
    if err != nil {
        log.Fatalf("Failed to create title video with background: %v", err)
    }
}

func createFinalVideo(fontDir string, fontName string, postMP3 string, titleMP3 string, titleScreenshotName string, titleAudioLength int, srtFile string, backgroundVideo string, outputFile string) {
	os.Setenv("FC_CONFIG_DIR", fontDir)
	os.Setenv("FONTCONFIG_PATH", fontDir)
	
	outputPath := filepath.Dir(outputFile)
	if err := os.MkdirAll(outputPath, os.ModePerm); err != nil {
		fmt.Printf("Error creating directories: %v\n", err)
		return
	}

	combineCmd := exec.Command("ffmpeg",
		"-i", "temp_video.mp4",
		"-i", postMP3,
		"-filter_complex", fmt.Sprintf("[1:a]adelay=%d|%d[a2];[0:a][a2]amix=inputs=2[a];[0:v]subtitles=%s:force_style='Outline=1,OutlineColour=&H000000&,FontName=%s,FontSize=11,Alignment=10'[v]", titleAudioLength*1000, titleAudioLength*1000, srtFile, fontName),
		"-map", "[v]",
		"-map", "[a]",
		"-c:v", "libx264",
		"-c:a", "aac",
		"-shortest", outputFile)
	err := combineCmd.Run()
	if err != nil {
		log.Fatalf("Failed to combine files: %v", err)
	}
	fmt.Printf("Output file created: %s\n", outputFile)
	
}

func CreateVideo(fontDir string, fontName string, postMP3 string, titleMP3 string, titleScreenshotName string, srtFile string, backgroundVideo string, subredditName string, postID string) {
	// File paths
	outputFile := "output/"+subredditName+"/"+postID+".mp4"
	if (fontName == "") {
		fontName = "ComicSansMS"
	}

	titleAudioLength := GetAudioLength(titleMP3) + 1
	postAudioLength := GetAudioLength(postMP3) + 1
	audioLength := postAudioLength + titleAudioLength
	createBaseVideo(audioLength, titleAudioLength, backgroundVideo, titleMP3, titleScreenshotName)
	createFinalVideo(fontDir, fontName, postMP3, titleMP3, titleScreenshotName, titleAudioLength, srtFile, backgroundVideo, outputFile)
}