import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="saran@R2003",
  database="ostlab1"
)
cursor = mydb.cursor()

name="saran"
rollno="2018139"
email="saran@gct.ac.in"
cgpa=10
cursor.execute("insert into students values (%s ,%s,%s,%s )",(name,rollno,email,cgpa))
cursor.execute("select * from students")
for X in cursor:
    print(X)

print(mydb)
mydb.close()