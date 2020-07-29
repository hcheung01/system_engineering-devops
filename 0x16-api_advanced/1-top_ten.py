#!/usr/bin/python3
"""
Python script
"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    params = {'limit': 10}
    headers = {'User-agent': 'BotHeiny'}
    try:
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False).json()
        data = response['data']['children']
        for listing in data:
            title = listing.get('data').get('title')
            print(title)
    except:
        print('None')
