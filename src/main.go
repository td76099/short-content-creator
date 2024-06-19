package main

import (
	"fmt"
	"os"
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
	LanguageCode	string	`yaml:"languageCode"`
	Voice			string	`yaml:"voice"`
}

type ContentConfig struct {
	GCPCreds	string				`yaml:"gcpCreds"`
	RedditCreds	string				`yaml:"redditCreds"`
	FontDir		string				`yaml:"fontDir"`
	Subreddits 	[]SubredditConfig	`yaml:"subreddits"`
}

type FileConfig struct {
	TitleFileName		string
	TitleAudioName		string
	TitleScreenshotName	string
	PostFileName		string
	PostAudioName		string
	TimingFileName		string
	SubtitleFileName	string
	BackgroundVideo		string
}

func main() {
	data, _ := ioutil.ReadFile("config.yaml")
	var contentConfig ContentConfig
	yaml.Unmarshal(data, &contentConfig)
	
	workdir := "tmp/"
	fileConfig := FileConfig {
		TitleFileName:			workdir+"title.txt",
		TitleAudioName:			workdir+"title.mp3",
		TitleScreenshotName:	workdir+"title.png",
		PostFileName:			workdir+"post.txt",
		PostAudioName:			workdir+"post.mp3",
		TimingFileName:			workdir+"post.pho",
		SubtitleFileName:		workdir+"post.srt",
		BackgroundVideo:		"backgrounds/mobile_gameplay_1.mp4",
	}
	
	for _, subreddit := range contentConfig.Subreddits {
		os.Mkdir(workdir, 0755)
		
		postID := CreateRedditText(subreddit, fileConfig)
		fmt.Println(postID)
		CreateTTS(subreddit.Voice, subreddit.LanguageCode, fileConfig.TitleFileName, fileConfig.TitleAudioName)
		CreateTTS(subreddit.Voice, subreddit.LanguageCode, fileConfig.PostFileName, fileConfig.PostAudioName)
		generateTiming(fileConfig, workdir)
		CreateSRT(fileConfig, GetAudioLength(fileConfig.TitleAudioName)+1)
		CreateVideo(contentConfig.FontDir, subreddit.Font, fileConfig, workdir, subreddit.Name, postID)
		
		os.RemoveAll(workdir)
	}
}

func generateTiming(fileConfig FileConfig, workdir string) {
	fmt.Println("generating timing")
	cmdResult := exec.Command("docker", "run", "--rm",
		"-v", "/mnt/g/Downloads3/short-content-creator/"+workdir+":/"+workdir,
		"--entrypoint", "python",
		"lowerquality/gentle",
		"/gentle/align.py",
		"/"+fileConfig.PostAudioName,
		"/"+fileConfig.PostFileName,
		"-o", "/"+fileConfig.TimingFileName)
	
	out, err := cmdResult.Output()
    if err != nil {
        fmt.Println(err.Error())
        return
    }

	// Print the output
	fmt.Println(string(out))
}