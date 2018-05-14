# -*- coding: utf-8 -*-
"""
Created on Mon May 14 23:26:50 2018

@author: rpuneet
"""

from subprocess import PIPE , Popen

temp = Popen(["git" , "init"] , stdout = PIPE , stderr = PIPE)
print(temp.communicate()[0].decode())

temp = Popen(["git" , "add" , "*"] , stdout = PIPE , stderr = PIPE)
print(temp.communicate()[0].decode())

temp = Popen(["git" , "commit" , "-m" , "Initialising project"] , stdout = PIPE , stderr = PIPE)
print(temp.communicate()[0].decode())

user_name = input("Enter github user name : ").strip()

temp = Popen(["curl" , "-u" , user_name , "https://api.github.com/user/repos -d" ,  " \'{ \" name\": \"Halite\" }\'"] , stdout = PIPE , stderr = PIPE)
print(temp.communicate()[0].decode())

temp = Popen(["git" , "remote" , "add" , "origin" , "https://github.com/"+user_name+"/Halite"] , stdout = PIPE , stderr = PIPE)
print(temp.communicate()[0].decode())

temp = Popen(["git" , "push" , "origin" , "master"] , stdout = PIPE , stderr = PIPE)
print(temp.communicate()[0].decode())