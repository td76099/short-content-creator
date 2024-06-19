package main

import (
	"encoding/json"
	"log"
	"os"
	"fmt"
	"html"
	"io/ioutil"
	"net/http"
	"net/url"
	"regexp"
	"strings"
	"github.com/playwright-community/playwright-go"
)

type RedditCredentials struct {
	ClientID     string `json:"clientID"`
	ClientSecret string `json:"clientSecret"`
	Username     string `json:"username"`
	Password     string `json:"password"`
	UserAgent    string `json:"userAgent"`
}

type TokenResponse struct {
	AccessToken string `json:"access_token"`
	TokenType   string `json:"token_type"`
	ExpiresIn   int    `json:"expires_in"`
	Scope       string `json:"scope"`
}

type PostData struct {
	Title 		string `json:"title"`
	URL   		string `json:"url"`
	SelfText 	string `json:"selfText"`
	ID			string `json:"id"`
}

type RedditResponse struct {
	Data struct {
		Children []struct {
			Data PostData `json:"data"`
		} `json:"children"`
	} `json:"data"`
}

var redditCreds RedditCredentials

func loadCreds() {
	data, _ := ioutil.ReadFile("creds/reddit.json")
	json.Unmarshal(data, &redditCreds)
}

func getOAuthToken() (string, error) {
	loadCreds()
	data := url.Values{}
	data.Set("grant_type", "password")
	data.Set("username", redditCreds.Username)
	data.Set("password", redditCreds.Password)

	req, err := http.NewRequest("POST", "https://www.reddit.com/api/v1/access_token", strings.NewReader(data.Encode()))
	if err != nil {
		return "", err
	}

	req.SetBasicAuth(redditCreds.ClientID, redditCreds.ClientSecret)
	req.Header.Set("User-Agent", redditCreds.UserAgent)
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("failed to get token: %s", resp.Status)
	}

	var tokenResponse TokenResponse
	err = json.NewDecoder(resp.Body).Decode(&tokenResponse)
	if err != nil {
		return "", err
	}

	return tokenResponse.AccessToken, nil
}

func getTopPosts(token string, subreddit string, usedIDFile string) (PostData, error) {
	var post PostData
	url := "https://oauth.reddit.com/r/"+subreddit+"/top/.json?t=month&limit=25&raw_json=1"

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return post, err
	}

	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("User-Agent", redditCreds.UserAgent)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return post, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return post, fmt.Errorf("failed to get top posts: %s", resp.Status)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return post, err
	}

	var redditResponse RedditResponse
	err = json.Unmarshal(body, &redditResponse)
	if err != nil {
		return post, err
	}

	return selectPost(usedIDFile, redditResponse), nil
}

func selectPost(usedIDFile string, redditResponse RedditResponse) PostData {
	data, err := os.ReadFile(usedIDFile)
	if err != nil {
		log.Println(err)
	}

	usedIDs := strings.Split(string(data), ",")
	fmt.Println(usedIDs)
	for _, redditPost := range redditResponse.Data.Children{
		newPost := true
		for _, id := range usedIDs {
			if (redditPost.Data.ID == id){
				newPost = false
				break
			}
		}
		if (newPost) {
			redditPost.Data.SelfText = cleanSelftext(redditPost.Data.SelfText)
			return redditPost.Data
		}
	}
	var post PostData
	return post

}

func cleanSelftext(text string) string {
	text = html.UnescapeString(text)
	text = strings.ReplaceAll(text, "\u200B", "") // zero-width character that shows up sometimes
	re := regexp.MustCompile(`[^\S\r]+`) // Matches any whitespace characters except newline
	text = re.ReplaceAllString(text, " ")
	re = regexp.MustCompile(`[\x00-\x1F\x7F-\x9F]`) // Matches unicode that might show up
	text = re.ReplaceAllString(text, "")

	return strings.TrimSpace(text)
}

func titleScreenshot(subreddit string, title string, titleScreenshotName string) {
	pw, err := playwright.Run()
    if err != nil {
        log.Fatalf("could not start Playwright: %v", err)
    }
    browser, err := pw.Chromium.Launch()
    if err != nil {
        log.Fatalf("could not launch browser: %v", err)
    }

	device := pw.Devices["Pixel 5"]
	context, err := browser.NewContext(playwright.BrowserNewContextOptions{
		Geolocation: &playwright.Geolocation{
			Longitude: 12.492507,
			Latitude:  41.889938,
		},
		Permissions:       []string{"geolocation"},
		Viewport:          device.Viewport,
		UserAgent:         playwright.String(device.UserAgent),
		DeviceScaleFactor: playwright.Float(device.DeviceScaleFactor),
		IsMobile:          playwright.Bool(device.IsMobile),
		HasTouch:          playwright.Bool(device.HasTouch),
	})
    if err != nil {
        log.Fatalf("could not create context: %v", err)
    }
    page, err := context.NewPage()
    if err != nil {
        log.Fatalf("could not create page: %v", err)
    }
	// Handle dialog event to dismiss popups automatically
	page.On("dialog", func(dialog playwright.Dialog) {
		log.Printf("Dialog detected: %s", dialog.Message())
		dialog.Dismiss()
	})

	_, err = page.Goto("https://reddit.com/r/"+subreddit+"/top/?t=month&limit=25&raw_json=1")
    if err != nil {
        log.Fatalf("could not go to URL: %v", err)
    }
	_, err = page.Evaluate(`
    document.querySelector("shreddit-experience-tree").style.display = "none";
	`)
	if err != nil {
		log.Fatalf("could not inject CSS to hide popup: %v", err)
	}
	// Use the CSS selector for the class "top-matter"
	temp_title := strings.ReplaceAll(title, "'", `\'`)
	postTitleElement := page.Locator(fmt.Sprintf("article[aria-label='%s']", temp_title))

	// Wait for the element to be visible
	err = postTitleElement.WaitFor()
	if err != nil {
		log.Fatalf("element not found: %v", err)
	}

	_, err = postTitleElement.Screenshot(playwright.LocatorScreenshotOptions{
		Path: &titleScreenshotName,
	})

    if err != nil {
        log.Fatalf("could not take screenshot: %v", err)
    }
    err = browser.Close()
    if err != nil {
        log.Fatalf("could not close browser: %v", err)
    }
    err = pw.Stop()
    if err != nil {
        log.Fatalf("could not stop Playwright: %v", err)
    }
}

func saveID(id string, idFile string) {
	f, err := os.OpenFile(idFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Println(err)
	}
	defer f.Close()

	if _, err := f.WriteString(fmt.Sprintf("%s,", id)); err != nil {
		log.Println(err)
	}
}

func CreateRedditText(subreddit SubredditConfig, titleFileName string, titleScreenshotName string, postFileName string) string {
	token, err := getOAuthToken()
	if err != nil {
		fmt.Println("Error getting OAuth token:", err)
		return ""
	}
	post, err := getTopPosts(token, subreddit.Name, subreddit.UsedIDFile)
	if err != nil {
		fmt.Println("Error getting top posts:", err)
		return ""
	}

	titleScreenshot(subreddit.Name, post.Title, titleScreenshotName)
	ioutil.WriteFile(titleFileName, []byte(post.Title), 0644)
	ioutil.WriteFile(postFileName, []byte(post.SelfText), 0644)
	saveID(post.ID, subreddit.UsedIDFile)
	
	return post.ID
}
