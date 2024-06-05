#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None.
    Invalid subreddits may return a redirect to search results.
    """
    request = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
        allow_redirects=False,
    )

    if request.status_code == 200:
        for get_data in request.json().get("data").get("children"):
            request_data = get_data.get("data")
            title = request_data.get("title")
            print(title)
    else:
        print(None)
