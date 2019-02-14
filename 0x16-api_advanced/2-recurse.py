#!/usr/bin/python3
"""
recursive function
"""
import requests

s = requests.Session()
s.headers.update({'User-Agent': 'Script'})
s.allow_redirects = False


def recurse(subreddit, hot_list=[]):
    """recursively grab subreddit"""

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    r = s.get(url).json()['data']
    try:
        for t in r['children']:
            hot_list.append(t['data']['title'])
        if r['after']:
            s.params = {'after': r['after']}
            return recurse(subreddit, hot_list)
        return hot_list
    except:
        return None
