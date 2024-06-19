package main

import (
	"fmt"
	"os/exec"
	"io/ioutil"
	"gopkg.in/yaml.v3"
)

type SubredditConfig struct {
	Name			string	`yaml:"name"`
	PostMinLength	int		`yaml:"postMinLength"`
	UsedIDFile		string	`yaml:"usedIDFile"`
	InstagramCreds	string	`yaml:"instagramCreds"`
	TiktokCreds		string	`yaml:"tiktokCreds"`
	YoutubeCreds	string	`yaml:"youtubeCreds"`
	Font			string	`yaml:"font"`
	Voice			string	`yaml:"voice"`
}

type ContentConfig struct {
	GCPCreds	string				`yaml:"gcpCreds"`
	RedditCreds	string				`yaml:"redditCreds"`
	FontDir		string				`yaml:"fontDir"`
	Subreddits 	[]SubredditConfig	`yaml:"subreddits"`
}

func main() {
	data, _ := ioutil.ReadFile("config.yaml")
	var contentConfig ContentConfig
	yaml.Unmarshal(data, &contentConfig)
	
	titleFileName := "title.txt"
	titleAudioName := "title.mp3"
	titleScreenshotName := "title.png"
	postFileName := "post.txt"
	postAudioName := "post.mp3"
	timingFileName := "post.pho"
	subtitleFileName := "post.srt"
	backgroundVideo := "videos/background/mobile_gameplay_1.mp4"
	subreddit := contentConfig.Subreddits[0]

	postID := CreateRedditText(subreddit, titleFileName, titleScreenshotName, postFileName)
	fmt.Println(postID)
	CreateTTS(subreddit.Voice, titleFileName, titleAudioName)
	CreateTTS(subreddit.Voice, postFileName, postAudioName)
	generateTiming(postFileName, postAudioName, timingFileName)
	CreateSRT(timingFileName, subtitleFileName, GetAudioLength(titleAudioName)+1)
	CreateVideo(contentConfig.FontDir, subreddit.Font, postAudioName, titleAudioName, titleScreenshotName, subtitleFileName, backgroundVideo, subreddit.Name, postID)
}

func generateTiming(postFileName string, postAudioName string, timingFileName string) {
	cmdResult := exec.Command("docker", "run", "--rm", "-v", "/mnt/g/Downloads3/short-content-creator:/tmp", "--entrypoint", "python", "lowerquality/gentle", "/gentle/align.py", "/tmp/"+postAudioName, "/tmp/"+postFileName, "-o", "/tmp/"+timingFileName)
	out, err := cmdResult.Output()
    if err != nil {
        fmt.Println(err.Error())
        return
    }

	// Print the output
	fmt.Println(string(out))
}