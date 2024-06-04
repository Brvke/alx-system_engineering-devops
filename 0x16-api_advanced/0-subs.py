#!/usr/bin/python3
"""
This module defines the function number_of_subscribers.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns:
    int: Number of subscribers or 0 if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/username)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0