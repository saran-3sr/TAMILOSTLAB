import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="System"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

import mysql.connector  
  
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "student",database="student")  
  
cur  = myconn.cursor()

# CERATE :

cur.execute("create table Students(Name varchar(20) not null, Rollno int(20) not null primary key, Age int(20) not null, Gender varchar(1) not null, Mail varchar(30) not null, Phone int(10) not null, CGPA varchar(4) not null)") 

sql = """insert into Students
    (Name,Rollno,Age,Gender,Mail,Phone,CGPA) 
    values (%s,%s,%s,%s,%s,%s,%s)"""

val = [
    ('John', 2018101 , 21 , 'M', 'j@gmail.com' , 992748328 , '9.5'),
    ('Sesila', 2018102 , 19 , 'F', 's@gmail.com' , 987654321 , '9.4'),
    ('Roman', 2018103 , 21 , 'M', 'r@gmail.com' , 927483346 , '8.5'),
    ('Dana', 2018104 , 23 , 'F', 'd@gmail.com' , 952463281 , '8.7'),
    ('Varun', 2018105 , 22 , 'M', 'v@gmail.com' , 929424398 , '9.9')
]

cur.executemany(sql,val) 
myconn.commit()
print(cur.rowcount, "was inserted.")

cur.execute("select * from Students")
for i in cur:
 print(i)

cur.execute("delete from Students where Name = 'Roman'")
myconn.commit()

print(cur.rowcount, "record affected")
sql = "update Students set CGPA = '8.6' where Name = 'Dana'"
cur.execute(sql)
myconn.commit()

print(cur.rowcount, "record affected")
