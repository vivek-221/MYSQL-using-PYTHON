import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="yarlagadda"
    )
d=mydb.cursor()
sql="DELETE FROM BASIC WHERE NAME='VIVEK'"
sql2="INSERT INTO BASIC(NAME,AGE) VALUES (%s,%s)"
val=("vivek","19")
sql1="SELECT * FROM BASIC ORDER BY AGE DESC"
d.execute(sql)
d.execute(sql2,val)
d.execute(sql1)
res=d.fetchall()

print(d.rowcount,"records deleted")
for x in res:
    print(x)
