import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="yarlagadda"
    )
d=mydb.cursor()
sql="SELECT * FROM BASIC ORDER BY NAME"
d.execute(sql)
res=d.fetchall()
for x in res:
    print(x)
