#!/usr/bin/python3
"""returns the information about an employess todo list based on employee_id"""
import requests
import sys
import csv


def todo_progress(employee_id):
    """returns the information about an employess todo list
    based on employee_id"""
    data_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(data_url, employee_id))
    data = user.json()
    name = data.get("name")

    todos = requests.get("{}/todos".format(data_url),
                         params={"userId": employee_id}).json()
    number_of_todos = len(todos)
    todos_finished = [task for task in todos if task["completed"]]
    number_of_finished_todos = len(todos_finished)

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, mode="w", newline="") as file:
        for task in todos:
            csv.writer(file).writerow([employee_id, name,
                                      str(task["completed"]), task["title"]])


if __name__ == "__main__":
    todo_progress(int(sys.argv[1]))
