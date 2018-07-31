'''
This is for all the version control stuffs.
'''

import os

from subprocess import PIPE , Popen

def init(repo_path):
    current_path = os.getcwd()
    os.chdir(repo_path)
    commandline = Popen(['git' , 'init'] , stdout = PIPE , stderr = PIPE)
    print()
    print(commandline.communicate()[0].decode())
    os.chdir(current_path)


def commit(repo_path , commit_message):
    current_path = os.getcwd()
    os.chdir(repo_path)
    commandline = Popen(['git' , 'commit' , '-m' , commit_message] , stdout = PIPE , stderr = PIPE)
    print()
    print(commandline.communicate()[0].decode())
    os.chdir(current_path)

def add(repo_path , *args):
    current_path = os.getcwd()
    os.chdir(repo_path)
    command = ['git' , 'add']
    command.extend(args)
    commandline = Popen(command , stdout = PIPE , stderr = PIPE)
    print()
    print(commandline.communicate()[0].decode())
    os.chdir(current_path)