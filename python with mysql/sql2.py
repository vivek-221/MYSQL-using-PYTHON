import mysql.connector
from mysql.connector import errorcode
mydb=mysql.connector.connect(
    host="127.0.0.1",
    auth_plugin='mysql_native_password',
    user="root",
    password="root"
    
    )
print(mydb)
