'''
This is the main file where the program is executed.
'''

import User

import LoginPage

import UserHomePage

import ProjectHomePage

import sys

import os

command_line = '/> '   # To be printed for a command.
current_user = None
current_project = None

os.system('clear')




while True:
    print()
    command = input(command_line)
    command = command.strip()

    # Exit when exit command is passed.
    if command == "exit":
        sys.exit(0)

    # Clear screen command.
    if command == "clear" or command == "cls":
        os.system('clear')
        continue


    if current_user == None:
        # We are at the login page.
        current_user = LoginPage.execute(command)
        if current_user != None:
            command_line = '/' + current_user.user_handle + '/> '
            os.system('clear')

    elif current_project == None:
        # We are at user home page
        current_project = UserHomePage.execute(command , current_user)

        if current_project == "LOGOUT":
            command_line = '/> '
            current_user = None
            current_project = None
            os.system('clear')
            continue
        elif current_project != None:
            command_line = command_line[:-3] + '/' + current_project.project_name + '/> '

    else:
        # We are at Project home page.
        response = ProjectHomePage.execute(command)
        
        if response == 'CLOSE':
            command_line = '/' + current_user.user_handle + '/> '
            current_project = None
            os.system('clear')
            continue

    # Update user json file.
    if current_user != None:
        current_user.update_json_file()

