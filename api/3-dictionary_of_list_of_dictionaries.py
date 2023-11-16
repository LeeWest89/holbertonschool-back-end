#!/usr/bin/python3
"""returns the information about an employess todo list based on employee_id"""
import json
import requests
import sys


def todo_progress():
    """returns the information about an employess todo list
    based on employee_id"""
    data_url = "https://jsonplaceholder.typicode.com"

    json_data = {}
    employee_id = 1
    while True:
        user = requests.get("{}/users/{}".format(data_url, employee_id))
        data = user.json()
        if "id" not in data:
            break
        name = data.get("username")

        todos = requests.get("{}/todos".format(data_url),
                             params={"userId": employee_id}).json()

        json_data[str(employee_id)] = [{
            "task": task["title"],
            "completed": task["completed"],
            "username": name} for task in todos
        ]

        employee_id += 1

    if json_data:
        with open("todo_all_employees.json", mode="w") as file:
            json.dump(json_data, file)


if __name__ == "__main__":
    todo_progress()
