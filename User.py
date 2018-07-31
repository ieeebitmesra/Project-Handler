""" 
This class contains all the features of a particular user. 
It loads the user data from the local directories given the user_handle and password
and stores the data of that user in the object.
"""

import json

import hashlib

import os

class User():


    def __init__(self , user_handle , password):
        ''' 
        Initialise a user object from the user_handle and password and load all the other
        user details from user json file.
        
        Parameters - 
            (string) user_handle - Handle of the user i.e. the user id.
            (string) password - Password of the user.
        Returns - 
            A user object after loading all the information from the user's json file. Or error code if any.
        '''

        self.user_handle = user_handle

        self.user_json_path = os.path.join(os.getcwd() , "User-Details" , "{}.json".format(user_handle) )
        
        # Check if file exists.
        if not os.path.exists(self.user_json_path):
            raise Exception("User doesn't exist.")

        with open(self.user_json_path , 'r') as user_info_file:
            user_information = json.load(user_info_file)


        self.current_password_hash = hashlib.sha256(password.encode()).hexdigest()

        if(self.current_password_hash != user_information['password_hash']):
            raise Exception("Incorrect password")
        

        self.user_name = user_information['user_name']
        self.project_list = user_information['project_list']
        self.current_task_list = user_information['current_task_list']

    def add_project(self , project):
        '''
        Add a project for this user.
        Parameters - 
            project - A project object.
        '''
        self.project_list.append(project.project_name)

    def update_json_file(self):
        '''Updates user's details in the json file.'''
        
        user_data = {
            'user_name' : self.user_name,
            'user_handle' : self.user_handle,
            'password_hash' : self.current_password_hash,
            'project_list' : self.project_list,
            'current_task_list' : self.current_task_list
        }

        with open(self.user_json_path , 'w') as user_info_file:
            json.dump(user_data , user_info_file)
        
        





    def _user_details(self):
        ''' A utility function which returns user details. '''
        return self.__dict__

