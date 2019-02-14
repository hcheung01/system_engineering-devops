#!/usr/bin/python3
"""
recursive function
"""
from requests import Session


s = Session()
s.headers.update({'User-Agent': 'Script'})
s.allow_redirects = False


def recurse(subreddit, hot_list=[]):
    """recursively grab subreddit"""

    print(hot_list)
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    r = s.get(url).json()
    for t in r['data']['children']:
        hot_list.append(t['data']['title'])
    if r['data']['after']:
        s.params = {'after': r['data']['after']}
        return recurse(subreddit, hot_list)
    else:
        return hot_list
