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


def save_to_csv(payload=None, payload2=None, file_name=None):
    """create new CSV file and load"""

    with open(file_name, 'w') as csvfile:
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


def save_to_json(payload=None, payload2=None, file_name=None):
    """send response data to a JSON file"""

    with open(file_name, 'w') as wfile:
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


def save_all_to_json(payload=None, payload2=None, file_name=None):
    """save all response object data to a JSON file"""

    with open(file_name, 'w') as wfile:
        data = {}
        for each in user:
            all_objs = []
            id = each.get('id')
            for arg in todo:
                d = OrderedDict()
                if id == arg.get('userId'):
                    d["username"] = each.get('username')
                    d['task'] = arg.get('title')
                    d['completed'] = arg.get('completed')
                    all_objs.append(d)
            data[id] = all_objs
        json.dump(data, wfile)


if __name__ == "__main__":
    import requests
    import json
    import csv
    from sys import argv
    from collections import OrderedDict

    try:
        payload = {'id': argv[1]}
        payload2 = {'userId': argv[1]}
        json_file = argv[1] + ".json"
        csv_file = argv[1] + ".csv"
    except:
        payload = {}
        payload2 = {}
        json_file = "todo_all_employees.json"

    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=payload).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=payload2).json()

    try:
        save_to_csv(user, todo, csv_file)
        save_to_json(user, todo, json_file)
        print_response(user, todo)
    except:
        save_all_to_json(user, todo, json_file)
