#!/usr/bin/python3
"""
Script to make request from an API
"""


def counter(completed=None):
    """Just to count completed task"""

    ct = 0
    for arg in todo:
        if arg.get('completed') is True:
            ct += 1
    return ct


def print_response(payload=None, payload2=None):
    """print response object"""

    print('Employee {} is done with tasks({}/{}):'.format(
        user[0].get('name'),
        counter(todo),
        len(todo)))

    for arg in todo:
        if arg.get('completed') is True:
            print("\t {}".format(arg.get('title')))


def to_csv(payload=None, payload2=None):
    """create new CSV file and load"""

    with open(argv[1] + ".csv", 'w') as csvfile:
        fieldnames = ["USER_ID",
                      "USERNAME",
                      "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for arg in todo:
            writer.writerow({"USER_ID": arg.get('userId'),
                             "USERNAME": user[0].get('username'),
                             "TASK_COMPLETED_STATUS": arg.get('completed'),
                             "TASK_TITLE": arg.get('title')})

if __name__ == "__main__":
    import requests
    import csv
    from sys import argv

    payload = {'id': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=payload).json()

    payload2 = {'userId': argv[1]}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=payload2).json()

    print_response(payload, payload2)
    to_csv(payload, payload2)
