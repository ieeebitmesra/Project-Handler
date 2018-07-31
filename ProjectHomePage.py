'''
This package is used to execute CLI commands for the Project home page.
'''


def help():
    print('''Commands -
    close - Closes the current project and goes back to user home page.''')

def execute(command):
    '''
    Executes the given command.
    
    Commands - 
        close - Closes the current project and goes back to user home page.

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

    else:
        print("Incorrect command.")

    return None
