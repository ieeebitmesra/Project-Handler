"""
A task class to hold all the information of a particular task.
"""

import os

import json

import Project

class Task:

    def __init__(self , task_name , project):

        self.task_name = task_name

        self.path = os.path.join( project.path , 'Tasks' )

        if not os.path.exists(self.path):
            os.mkdir(self.path)
        
        self.json_path = os.path.join(self.path , '{}.json'.format(task_name))

        if not os.path.exists(self.json_path):
            raise Exception("Path doesn't exist.")
        
        with open(self.json_path , 'r') as json_file:
            task_data = json.load(json_file)
        
        self.description = task_data['description']
        self.parent_file = task_data['parent_file']
        self.assigned_to = task_data['assigned_to']
        self.history = task_data['history']
        self.status = task_data['status']


    def update_json(self):

        task_data = {}
        task_data['name'] = self.task_name
        task_data['description'] = self.description
        task_data['parent_file'] = self.parent_file
        task_data['assigned_to'] = self.assigned_to
        task_data['history'] = self.history
        task_data['status'] = self.status

        with open(self.json_path , 'w') as out:
            json.dump(task_data , out)
        
    def display_CLI(self , index ):
        print(
            "{index}. {task_name}".format(
                index = index,
                task_name = self.task_name
            )
        )

    def display_details_CLI(self):
        print(
            '''
Name - {task_name}
Description - {description}
Status - {status}
Associated File - {file}
Assigned to - {assign}
            '''.format(
                task_name = self.task_name,
                description = self.description,
                status = self.status,
                file = self.parent_file,
                assign = self.assigned_to
            )
        )