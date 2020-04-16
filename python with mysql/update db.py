import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="yarlagadda"
    )
d=mydb.cursor()
sql="UPDATE BASIC SET AGE='17' WHERE NAME='bhavya'"
d.execute(sql)
sql2="DELETE FROM BASIC WHERE NAME='VIVEK'"
d.execute(sql2)
sql3="INSERT INTO BASIC(NAME,AGE) VALUES(%s,%s)"
val=("vivek","19")
d.execute(sql3,val)
sql1="SELECT * FROM BASIC ORDER BY AGE"
d.execute(sql1)
res=d.fetchall()
for x in res:
    print(x)
mydb.commit()
print('updated')


