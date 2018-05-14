# -*- coding: utf-8 -*-
"""
Created on Sat May 12 19:47:43 2018

@author: rpuneet
"""
from hashlib import sha256

class User:
    def __init__(self , user_name = "" , user_id = "" , user_password_sha256 = sha256("")):
        self.user_name = user_name
        self.user_id = user_id
        self.user_password_sha256 = user_password_sha256
        self.project_list = []
        self.current_task_list = []
        self.current_project = None
    
    