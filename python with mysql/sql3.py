import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE MYDATABASE")
print("database named bhavya successfully")
