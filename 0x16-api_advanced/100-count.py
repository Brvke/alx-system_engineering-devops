#!/usr/bin/python3
'''Script to recursively query the reddit API to get
a list of hot topic titles'''

import requests
import re

def count_words(subreddit, word_list, count=0, after=""):
    '''Function to recursively query the Reddit API and parse
    the title of all the hot topics'''

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'subreddit.subscriber.counter:v1.0'}

    params = {
        "limit": 100,
        "after": after,
        count: count
    }

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.get("data")
    after = data.get("after")
    count += int(data.get("dist"))
    for child in data.get("children"):
        title = child.get("title")
        for el in word_list:
            word_list[el] += [m.start() for m in re.finditer(el, title)]

    return word_list