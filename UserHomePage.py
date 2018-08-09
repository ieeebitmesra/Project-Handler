'''
All the commands of user home page are executed here.
'''

import User

import Project

import os

import json

import VCS


def help():
    print('''Commands - 
    create - Creates a new project.
    open project_name - opens the given project.
    ls -p - lists all the projects user is contributing to.
    ls -t - lists all the tasks user has taken.
    logout - logs out the current user.
    ''')



def create_new_project(user , project_head , project_name , project_brief_description):
    '''
    Creates a new file named {project_name}.json in the Projects directory with all default
    value for the project object fields. Also , add the project to the project list of the user
    who created it.

    Parameters -
        user - User object.
        project_head - Admin of the project.
        project_name - Name of the project.
        project_brief_description - A brief description of what is the purpose of the project.
    '''
    
    project_data = {}
    project_data['project_head'] = project_head
    project_data['project_name'] = project_name
    project_data['project_brief_description'] = project_brief_description
    project_data['contributers'] = [project_head]
    project_data['task_list'] = []
    project_data['quick_notes'] = []
    
    os.mkdir(os.path.join(os.getcwd() , 'Projects' , project_name))

    with open(os.path.join(os.getcwd() , 'Projects' , project_name , '{}.json'.format(project_name) ) , 'w') as project_file:
        json.dump(project_data , project_file)
    
    VCS.init( os.path.join(os.getcwd() , 'Projects' , project_name) )


    user.add_project(Project.Project(project_name))

def execute(command , user):
    '''
    Executes the given command.
    
    Commands - 
        create - Creates a new project.
        open project_name - opens the given project.
        ls -p - lists all the projects user is contributing to.
        ls -t - lists all the tasks user has taken.
        userDetails - prints details of the user.
        logout - logs out the current user.
    
    Parameters -
        command - the given command.
        user - an instance of user object.
    Returns - 
        Project object for open command , None otherwise.
    '''

    commands = command.split(' ')
    
    if commands[0] == 'userDetails':
        user_details = user._user_details()


    elif commands[0] == 'open':
        try:
            project = Project.Project(command[5:].strip())
            if user.user_handle not in project.contributers:
                print("You are not allowed to work on this project. Ask admin to add you.")
                return None
            return project
        except:
            print("Error in openning project.")
            return None

    elif commands[0] == 'ls':
        if len(commands) != 2:
            help()
            return None
        if commands[1] == '-p' or commands[1] == '--projects':
            project_list = user.project_list
            for i in range(len(project_list)):
                print("{}. {}".format(i + 1 , project_list[i]))
        elif commands[1] == '-t' or commands[1] == '--tasks':
            task_list = user.current_task_list
            for i in range(len(task_list)):
                print("{}. {}".format(i + 1, task_list[i]))
        else:
            help()
            return None
    elif commands[0] == 'logout':
        if len(commands) != 1:
            help()
            return None
        return "LOGOUT"

    elif commands[0] == 'help':
        help()
        return None

    elif commands[0] == 'create':
        if len(commands) != 1:
            help()
            return None
        # Create a new project. With project head as the current user.
        project_head = user.user_handle
        project_name = input("Enter Project name : ")
        project_brief_description = input("Enter a brief project description : ")
        create_new_project(user , project_head , project_name , project_brief_description)

    else:
        print("Incorrect command.")
        
    return None
