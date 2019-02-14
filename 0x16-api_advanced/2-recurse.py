#!/usr/bin/python3
"""
recursive function
"""
from requests import Session


def recurse(subreddit, hot_list=[]):
    """recurse the api"""

    print(hot_list)
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    s = Session()
    s.headers.update({'User-Agent': 'Honey'})
    s.allow_redirects = False

    data = s.get(url).json()['data']
    children = data['children']
    for t in children:
        hot_list.append(t['data']['title'])
    after = data['after']
    if after:
        s.params = {'after': after}
        return recurse(subreddit, hot_list)
    return hot_list or None
