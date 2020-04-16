import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="yarlagadda"
    )
d=mydb.cursor()

d.execute("CREATE TABLE BASIC(NAME VARCHAR(10),AGE VARCHAR(10))")

print(mycursor.rowcount, "record inserted.")
