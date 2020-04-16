import mysql.connector
mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="vivek"
    )
mycursor=mydb.cursor()
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)
