import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="vivek"
    )
d=mydb.cursor()
sql="DROP TABLE student"
d.execute(sql)
