import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="yarlagadda"
    )
d=mydb.cursor()
d.execute("SELECT * FROM BASIC ")
res=d.fetchall()
for x in res:
    print(x)
