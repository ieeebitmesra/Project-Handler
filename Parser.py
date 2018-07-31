"""
This is a parser package for the Command Line Interface.
"""


class Parser:

    def __init__(self , description):
        self.description = description
        self.commands = []
    




class Commands:

    def __init__(self , argument , funtion_on_call):
        self.argument = argument
        self.funtion_on_call = funtion_on_call

    def execute(self , args):
        funtion_on_call