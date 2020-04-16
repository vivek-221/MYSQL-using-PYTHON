# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:25:28 2020

@author: vivek
"""

import mysql.connector
mydb=mysql.connector.connect(
    host="127.0.0.1",
    auth_plugin='mysql_native_password',
    user="root",
    password="root"
    
    )
print(mydb)