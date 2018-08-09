'''
This file contains the project class which holds information of a particuler project.
It loads project details from the list of projects in user information.
'''

import json

import os

import User

import Task

import VCS

class Project:

    def __init__(self , project_name):
        '''
        Opens a {project}.json file from the project folder and 
        initialises a project object.

        Parameters - 
            project_name - Name of the project to open.
        '''

        self.project_name = project_name

        self.project_json_path = os.path.join(os.getcwd() , 'Projects' , project_name , '{}.json'.format(project_name) )

        self.path = os.path.join(os.getcwd() , 'Projects' , project_name )

        if not os.path.exists(self.project_json_path):
            raise Exception("No such file exists.")
        
        with open(self.project_json_path , 'r') as project_file:
            project_data = json.load(project_file)
        
        self.task_list = project_data['task_list']
        self.project_head = project_data['project_head']
        self.project_brief_description = project_data['project_brief_description']
        self.contributers = project_data['contributers']
        self.quick_notes = project_data['quick_notes']

    
    def add_task(self , task_name , description , parent_file):
        
        task_data = {}
        task_data['name'] = task_name
        task_data['description'] = description
        task_data['parent_file'] = parent_file
        task_data['assigned_to'] = ""
        task_data['history'] = []
        task_data['status'] = 'to-do'

        task_path = os.path.join(os.getcwd() , 'Projects' , self.project_name , 'Tasks')
        if(not os.path.exists(task_path)):
            os.mkdir(task_path)
        
        parent_file = os.path.join(self.path , parent_file)
        if not os.path.exists(parent_file):
            temp = open(parent_file , 'w')
            temp.close()

        task_json_path = os.path.join(task_path , '{}.json'.format(task_name))

        with open(task_json_path , 'w') as out:
            json.dump(task_data , out)
        
        self.task_list.append(task_name)
    

    def remove_task(self , task_name):

        self.task_list.remove(task_name)
        
        task_path = os.path.join(
            os.getcwd(), 'Projects', self.project_name, 'Tasks')

        if(not os.path.exists(task_path)):
            os.mkdir(task_path)

        task_json_path = os.path.join(task_path, '{}.json'.format(task_name))

        if not os.path.exists(task_json_path):
            raise Exception("Task does not exist.")
        
        os.remove(task_json_path)

    def get_task_list(self):
        task_list = []
        
        for tasks in self.task_list:
            task_list.append(Task.Task(tasks , self))

        return task_list

    def update_json_file(self):

        project_data = {}
        project_data['project_head'] = self.project_head
        project_data['project_name'] = self.project_name
        project_data['project_brief_description'] = self.project_brief_description
        project_data['contributers'] =self.contributers
        project_data['task_list'] = self.task_list
        project_data['quick_notes'] = self.quick_notes

        with open(os.path.join(os.getcwd(), 'Projects', self.project_name, '{}.json'.format(self.project_name)), 'w') as project_file:
            json.dump(project_data, project_file)

    def add_user(self , user_handle):
        user_json_path = os.path.join(os.getcwd() , 'User-Details' , '{}.json'.format(user_handle))
       
        if not os.path.exists(user_json_path):
            raise Exception("User doesn't exist.")

        user_data = {}
        with open(user_json_path , 'r') as user_json:
            user_data = json.load(user_json)
        user_data['project_list'].append(self.project_name)

        with open(user_json_path, 'w') as user_json:
            json.dump(user_data , user_json)

        self.contributers.append(user_handle)

    def remove_user(self , user_handle):
        user_json_path = os.path.join(
            os.getcwd(), 'User-Details', '{}.json'.format(user_handle))

        if not os.path.exists(user_json_path):
            raise Exception("User doesn't exist.")

        user_data = {}
        with open(user_json_path, 'r') as user_json:
            user_data = json.load(user_json)

        if self.project_name not in user_data['project_list']:
            raise Exception("Project doesn't exist for the given user.")

        user_data['project_list'].remove(self.project_name)

        with open(user_json_path, 'w') as user_json:
            json.dump(user_data, user_json)

        if user_handle not in self.contributers:
            raise Exception("This user is not a contributer.")
        self.contributers.remove(user_handle)

    def assign_task(self, task_name , user):
        
        if task_name not in self.task_list:
            raise Exception("Task doesn't exist.")
        try:
            task = Task.Task(task_name , self)
        except:
            raise Exception("Error in openning task.")

        if task.assigned_to != '':
            
            raise Exception("Task already assigned to someone.")

        task.assigned_to = user.user_handle
        task.history.append("Assigned to - {} , Status - {}".format(task.assigned_to , task.status))
        task.update_json()
        user.current_task_list.append(task_name)

    def submit_task(self , task_name , user , status):
        
        if task_name not in self.task_list:
            raise Exception("Task doesn't exist.")
        try:
            task = Task.Task(task_name, self)
        except:
            raise Exception("Error in openning task.")

        if task.assigned_to != user.user_handle:
            raise Exception("You don't have this task.")

        task.assigned_to = ""
        user.current_task_list.remove(task.task_name)
        task.history.append(
            "Submitted by - {} , Status - {}".format(user.user_handle, task.status))

        if task.status == status:
            task.update_json()
            return
        
        task.status = status
        try:
            VCS.add(self.path , task.parent_file)
            VCS.commit(self.path , "{} , Status - {}".format(task_name , status))
        except:
            raise Exception("VCS Error")
        task.update_json()


