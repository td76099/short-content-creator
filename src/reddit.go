package main

import (
	"encoding/json"
	"fmt"
	"html"
	"io/ioutil"
	"net/http"
	"net/url"
	"regexp"
	"strings"
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

func getTopPosts(token string, subreddit string) (PostData, error) {
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

	// for _, post := range redditResponse.Data.Children {
	// 	fmt.Printf("Title: %s\nURL: %s\nContent: %s\n\n", post.Data.Title, post.Data.URL, post.Data.SelfText)
	// }

	post = redditResponse.Data.Children[4].Data
	post.SelfText = cleanSelftext(post.SelfText)

	return post, nil
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
