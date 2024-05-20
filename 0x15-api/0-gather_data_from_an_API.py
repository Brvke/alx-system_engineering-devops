#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = "https://jsonplaceholder.typicode.com"
        employee_id = int(sys.argv[1])
        user = requests.get(
            "{}/users/{}".format(url, employee_id)).json()
        todos = requests.get(
            "{}/users/{}/todos/".format(url, employee_id)).json()

        NUMBER_OF_DONE_TASKS = 0
        TOTAL_NUMBER_OF_TASKS = ""
        for todo in todos:
            if todo['completed']:
                NUMBER_OF_DONE_TASKS += 1
                TOTAL_NUMBER_OF_TASKS += "\t {}\n".format(todo.get('title'))
        print(
            "Employee {} is done with tasks({}/{}):"
            .format(user.get('name'),  NUMBER_OF_DONE_TASKS, len(todos)))

        print(TOTAL_NUMBER_OF_TASKS[:-1])

    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
