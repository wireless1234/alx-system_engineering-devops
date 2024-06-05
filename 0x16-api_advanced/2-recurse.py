#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Prototype: def recurse(subreddit, hot_list=[])
    You may change the prototype, but it must be able to be called
    with just a subreddit supplied. AKA you can add a counter,
    but it must work without supplying a starting value in the main.
    If not a valid subreddit, return None.
    """
    request = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if request.status_code == 200:
        for get_data in request.json().get("data").get("children"):
            request_data = get_data.get("data")
            title = request_data.get("title")
            hot_list.append(title)
        after = request.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None