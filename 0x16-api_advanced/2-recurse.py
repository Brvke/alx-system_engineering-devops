#!/usr/bin/python3
"""Function to recursively query hot posts in a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ returns a list containing the titles
    of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python:reddit_scraper:v1.0 (by /u/GuidanceOk8279)'}
    
    params = {
        "after": after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    for thread in results.get("children"):
        hot_list.append(thread.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
