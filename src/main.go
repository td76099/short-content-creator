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
	subreddit := contentConfig.Subreddits[0]
	postID := CreateRedditText(subreddit)
	CreateTTS(subreddit.Voice)
	generateTiming()
	CreateSRT("output.pho")
	CreateVideo(contentConfig.FontDir, subreddit.Font, "videos/background/mobile_gameplay_1.mp4", subreddit.Name, postID)
}

func generateTiming() {
	cmdResult := exec.Command("docker", "run", "--rm", "-v", "/mnt/g/Downloads3/short-content-creator:/tmp", "--entrypoint", "python", "lowerquality/gentle", "/gentle/align.py", "/tmp/output.mp3", "/tmp/output.txt", "-o", "/tmp/output.pho")
	out, err := cmdResult.Output()
    if err != nil {
        fmt.Println(err.Error())
        return
    }

	// Print the output
	fmt.Println(string(out))
}