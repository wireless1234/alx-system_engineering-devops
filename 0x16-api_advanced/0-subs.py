#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
    Invalid subreddits may return a redirect to search results.
    """
    request = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        allow_redirects=False,
    )

    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
