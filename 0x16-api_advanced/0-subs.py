#!/usr/bin/python3
# queries the Reddit API and returns the number of subscribers
import requests


def number_of_subscribers(subreddit):
    """return total subscribers of reddit's subreddit"""

    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    try:
        response = requests.get(url,
                                headers={'User-agent': 'your bot 0.1'},
                                allow_redirects=False).json()
        return response['data'].get('subscribers')
    except:
        return 0
