#!/usr/bin/python3
"""Function to print the titles of the first 10 hot posts for a given subreddit."""

import requests

VERSION = "1.0.0"

def top_ten(subreddit):
    """Fetch and print the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': f'python:reddit_scraper:v{VERSION} (by /u/GuidanceOk8279)'
    }
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        print(None)