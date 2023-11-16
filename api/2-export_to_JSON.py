#!/usr/bin/python3
"""returns the information about an employess todo list based on employee_id"""
import json
import requests
import sys


def todo_progress(employee_id):
    """returns the information about an employess todo list
    based on employee_id"""
    data_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(data_url, employee_id))
    data = user.json()
    name = data.get("username")

    todos = requests.get("{}/todos".format(data_url),
                         params={"userId": employee_id}).json()
    todos_finished = [task for task in todos if task["completed"]]

    json_file = "{}.json".format(employee_id)
    json_data = {str(employee_id): [{
        "task": task["title"],
        "completed": task["completed"],
        "username": name} for task in todos
    ]}
    with open(json_file, mode="w") as file:
        json.dump(json_data, file)


if __name__ == "__main__":
    todo_progress(int(sys.argv[1]))
