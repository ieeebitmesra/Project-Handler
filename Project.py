'''
This file contains the project class which holds information of a particuler project.
It loads project details from the list of projects in user information.
'''

import json

import os


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

        if not os.path.exists(self.project_json_path):
            raise Exception("No such file exists.")
        
        with open(self.project_json_path , 'r') as project_file:
            project_data = json.load(project_file)
        
        self.task_list = project_data['task_list']
        self.project_head = project_data['project_head']
        self.project_brief_description = project_data['project_brief_description']
        self.contributers = project_data['contributers']
        self.quick_notes = project_data['quick_notes']

    
        