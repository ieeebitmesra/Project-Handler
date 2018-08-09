'''
This package is used to execute CLI commands for the Project home page.
'''

import User

import Project

import Task

def help():
    print('''Commands -
    close - Closes the current project and goes back to user home page.
    create - Creates a new task.
    remove -t task_name - removes the given task.
    ls -t - Displays the current list of tasks.
    ls -t task_name - Displays the details of the given task.
    ls -c - lists all the contributers of the current project.
    add user_handle - Add the given user to the project.
    remove -u user_handle - Removes the given user from the project.
    take -t task_name - Assign task_name to yourself.
    submit status task_name - submit task_name with the updated status of the task.
    ''')



def execute(command , user , project):
    '''
    Executes the given command.
    
    Commands - 
        close - Closes the current project and goes back to user home page.
        create - Creates a new task.
        remove -t task_name - removes the given task.
        ls -t - Displays the current list of tasks.
        ls -t task_name - Displays the details of the given task.
        ls -c - lists all the contributers of the current project.
        add user_handle - Add the given user to the project.
        remove -u user_handle - Removes the given user from the project.
        take -t task_name - Assign task_name to yourself.
        submit status task_name - submit task_name with the updated status of the task.

    Parameters -
        command - the given command.
    Returns - 
        response of the given command.
    '''

    commands = command.split(' ')

    if commands[0] == 'help':
        help()

    elif commands[0] == 'close':
        return "CLOSE"
    
    elif commands[0] == 'create':
        if len(commands) != 1:
            help()
            return None
        task_name = input("Enter Task Name : ")
        description = input("Enter the task description : ")
        parent_file = input("Enter the file name this task is associated to : ")
        project.add_task(task_name , description , parent_file)

    elif commands[0] == 'remove':
        if len(commands) < 3:
            help()
            return None
        if commands[1] == "-t":
            try:
                project.remove_task(command[10:].strip())
            except:
                print("Task doesn't exist.")
        elif commands[1] == '-u':
            if user.user_handle != project.project_head:
                print("You are not authorised to remove users.")
                return None

            try:
                project.remove_user(commands[2])
            except:
                print("This user is not a contributer.")
        else:
            help()
            return None
    elif commands[0] == 'ls':
        if len(commands) == 2 and commands[1] == '-c' or commands[1] == '--contributers':
            contributers = project.contributers
            for i in range(len(contributers)):
                print("{}. {}".format(i + 1, contributers[i]))
            return None
        if len(commands) == 2 and (commands[1] == '-t' or commands[1] == '--task'):
            task_list = project.get_task_list()
            # print("   Task Name")
            for i in range(len(task_list)):
                task_list[i].display_CLI(i + 1)
        elif len(commands) >= 3 and commands[1] == '-t':
            task_name = command[6:].strip()
            if task_name not in project.task_list:
                print("Task doesn't exist.")
                return None
            Task.Task(task_name , project).display_details_CLI()
        else:
            help()
            return None

    elif commands[0] == 'add':
        if len(commands) != 2:
            return None
        try:
            project.add_user(commands[1])
        except:
            print("User doesn't exist.")

    elif commands[0] == 'take':
        if len(commands) <= 2:
            help()
            return None
        if(commands[1] != '-t'):
            help()
            return None
        try:
            project.assign_task(command[8:].strip() , user)
        except:
            print("One of the following errors occured-\n1. Task doesn't exist.\n2. Error in opening the task.\n3. Task is already assigned to someone.")

    elif commands[0] == 'submit' and len(commands) > 2:
        status = commands[1]
        task_name = ""
        for i in range(2 , len(commands) - 1):
            task_name += commands[i] + " "
        task_name += commands[len(commands) - 1]
        task_name.strip()
        try:
            project.submit_task(task_name , user , status)
        except:
            print("One of the following errors occured-\n1. Task doesn't exist.\n2. Error in opening the task.\n3. You don't have this task.")


    else:
        print("Incorrect command.")

    return None
