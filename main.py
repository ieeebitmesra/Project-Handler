'''
This is the main file where the program is executed.
'''

import User

import LoginPage

command_line = '>'   # To be printed for a command.
current_user = None


while True:
    
    #slash_count = command_line.count('/')   # This is to check where is the user currently.
    command = input(command_line)

    if current_user == None:
        # We are at the login page.
        current_user = LoginPage.execute(command)
        if current_user != None:
            command_line = '/' + current_user.user_handle + '>'

    '''
    elif slash_count == 1:
        # We are at the home of user. i.e. No active projects.
        UserHome.execute(command)
    else:
        # We are inside a project.
        ProjectPage.execute(command)'''
