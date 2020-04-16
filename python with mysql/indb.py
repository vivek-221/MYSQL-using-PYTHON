import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="yarlagadda"
    )
d=mydb.cursor()
sql="INSERT INTO BASIC(NAME,AGE) VALUES(%s,%s)"
val=[("vivek","18"),("bhavya","16"),("hari","44"),("madhavi","43"),("sambasiva","72"),("aruna","69")]

d.executemany(sql,val)
mydb.commit()
print(d.rowcount, "record inserted.")
