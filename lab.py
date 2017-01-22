from __future__ import print_function
import os
import requests
import json
from termcolor import colored


class Todofun():

    def get_all_tasks(self):
        print ('-*-*' * 18)
        print(" " * 10 + "MY TASKS")
        print ('-*-*' * 18)
        resp = requests.get('http://jsonplaceholder.typicode.com/todos/')
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        data = json.loads(resp.text)
        for index, title in enumerate(data):
            print(str(index + 1) + " - " + title['title'])

    def get_task_details(self, task_id):
        print ('-*-*' * 18)
        print(" " * 10 + "TASK DETAILS")
        print ('-*-*' * 18)
        resp = requests.get('http://jsonplaceholder.typicode.com/todos/' + str(task_id))
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        task_data = json.loads(resp.text)
        if not task_data:  # Check if any data has been retrieved
            print("Try again using another id")
            return
        print("Task id: " + str(task_data['id']))
        print("Title: " + task_data['title'])
        
    def create_task(self, data):
        print("<" + "--"* 10 + "Creating task" + "--"* 10 + ">")
        resp = requests.post('http://jsonplaceholder.typicode.com/todos/', data = data)
        if resp.status_code == 201:
            task_details = json.loads(resp.text)
            print("Task {0} created succesfully".format(task_details['title']))
        else:
            print("Error occured creating task")

        

    def edit_task(self, task_id, data):
        print("<" + "--"* 10 + "Editing task" + "--"* 10 + ">" )
        resp = requests.put('http://jsonplaceholder.typicode.com/todos/' + str(task_id), data = data)
        if resp.status_code == 200:
            task_details = json.loads(resp.text)
            print("Task {0} edited succesfully".format(task_details['title']))
        else:
            print("Error occured editing task")


    def mark_finished(self, task_id):
        print("*" * 10 + "Task finished!!" + "*" * 10)
        resp = requests.delete('http://jsonplaceholder.typicode.com/todos/' + str(task_id))
        if resp.status_code == 200:
            task_details = json.loads(resp.text)
            print("Task completed succesfully")
        else:
            print("Error occured deleting task")

   #{u'completed': False, u'userId': 1, u'id': 1, u'title': u'delectus aut autem'}
   #{
 #"userId": 1,
  #"id": 5,title": "laboriosam mollitia et enim quasi adipisci quia provident illum","completed": false
