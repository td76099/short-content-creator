package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"time"
	"strings"
)

// WordInfo represents the structure of each word information in the JSON
type WordInfo struct {
	Start       float64 `json:"start"`
	End         float64 `json:"end"`
	AlignedWord string  `json:"alignedWord"`
	Word		string	`json:"word"`
}

// JsonData represents the overall JSON structure
type JsonData struct {
	Words []WordInfo `json:"words"`
}

// ConvertJSONToSRT converts the JSON data to SRT format and writes to a file
func convertJSONToSRT(jsonData JsonData, outputSrt string, offset int) error {
	file, err := os.Create(outputSrt)
	if err != nil {
		return err
	}
	defer file.Close()

	index := 1
	for _, wordInfo := range jsonData.Words {
		if wordInfo.Start > 0 {
			startTime := int(wordInfo.Start * 1000)+(offset*1000)
			endTime := int(wordInfo.End * 1000)+(offset*1000)
			_, err := fmt.Fprintf(file, "%d\n%s --> %s\n%s\n\n",
				index,
				formatTime(startTime),
				formatTime(endTime),
				strings.ToUpper(wordInfo.Word))
			if err != nil {
				return err
			}
			index++
		}
	}

	return nil
}

// formatTime formats the time in milliseconds to SRT time format
func formatTime(milliseconds int) string {
	duration := time.Duration(milliseconds) * time.Millisecond
	hours := duration / time.Hour
	duration -= hours * time.Hour
	minutes := duration / time.Minute
	duration -= minutes * time.Minute
	seconds := duration / time.Second
	duration -= seconds * time.Second
	millis := duration / time.Millisecond

	return fmt.Sprintf("%02d:%02d:%02d,%03d", hours, minutes, seconds, millis)
}

func CreateSRT(fileConfig FileConfig, offset int) {
	// Replace "input.json" with the path to your input JSON file
	data, err := ioutil.ReadFile(fileConfig.TimingFileName)
	if err != nil {
		fmt.Println("Error reading JSON file:", err)
		return
	}

	var jsonData JsonData
	err = json.Unmarshal(data, &jsonData)
	if err != nil {
		fmt.Println("Error parsing JSON data:", err)
		return
	}

	err = convertJSONToSRT(jsonData, fileConfig.SubtitleFileName, offset)
	if err != nil {
		fmt.Println("Error converting JSON to SRT:", err)
	}
}
