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


def to_json(payload=None, payload2=None):
    """send response data to a JSON file"""

    with open(argv[1] + '.json', 'w') as wfile:
        d = OrderedDict()
        all_objs = []
        for arg in todo:
            d['task'] = arg.get('title')
            d['completed'] = arg.get('completed')
            d["username"] = user[0].get('username')
            all_objs.append(d)
            d = OrderedDict()
        data = {
            argv[1]: all_objs
        }
        json.dump(data, wfile)


if __name__ == "__main__":
    import requests
    import json
    import csv
    from sys import argv
    from collections import OrderedDict

    payload = {'id': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=payload).json()

    payload2 = {'userId': argv[1]}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=payload2).json()

    print_response(user, todo)
    to_csv(user, todo)
    to_json(user, todo)
