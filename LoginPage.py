'''
All the commands of the login page are executed here.
'''

import hashlib

import User

import os

import json

def create_new_user(user_handle , user_name , password):
    '''
    This function is used to create a new user given the details of the user.
    It creates a {user_handle}.json file with the given details.
    project_list and current_task_list are initially empty. These are lists of respective objects.
    We store sha256 hash of the password.
    
    Parameters -
        (string) user_handle - Handle of the user i.e. the user id.
        (string) user_name - Name of the user.
        (string) password - Password of the user.
    Return - 
        (int) - error code if any, 0 if all ok.
    '''

    user_json_path = os.path.join(os.getcwd() , "User-Details" , "{}.json".format(user_handle) )

    # Check if the user already exists.
    if os.path.exists(user_json_path):
        return 1

    user_information = {
        'user_name' : user_name,
        'user_handle' : user_handle,
        'password_hash' : hashlib.sha256(password.encode()).hexdigest(),
        'project_list' : [],
        'current_task_list' : []
    }

    with open(user_json_path , 'w') as user_info_file:
        json.dump(user_information , user_info_file)
    
    return 0
    



def execute(command):
    '''
    Executes the given command.
    
    Commands - 
        login user_handle password - login user_handle and return the user object.
        create - creates a new account.
    
    Parameters -
        command - the given command.
    Returns - 
        User object for login and None for create.
    '''

    commands = command.split(' ')
    
    if commands[0] == 'create':
        user_handle = input("Enter user handle : ")
        user_name = input("Enter user name : ")
        password = input("Enter Password : ")
        create_new_user(user_handle , user_name , password)

    elif commands[0] == 'login':
        if len(commands) != 3:
            print("Incorrect login command. Use - login <user_handle> <password>")
            return None
        
        try:
            user = User.User(commands[1] , commands[2])
            return user
        except:
            print("Incorrect Login Credentials.")
            return None


    else:
        print("Incorrect Command.")

    return None

