import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="24062002",
    database="student_db"
)

cursor = connection.cursor()

def create_student(first_name, last_name, age, grade):
    sql = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, age, grade)
    cursor.execute(sql, values)
    connection.commit()
    print("Student created successfully")

def read_students():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def update_student(student_id, grade):
    sql = "UPDATE students SET grade = %s WHERE id = %s"
    values = (grade, student_id)
    cursor.execute(sql, values)
    connection.commit()
    print("Student updated successfully")

def delete_student(student_id):
    sql = "DELETE FROM students WHERE id = %s"
    value = (student_id,)
    cursor.execute(sql, value)
    connection.commit()
    print("Student deleted successfully")

while True:
    print("\n-- Student Database --")
    print("1. Create Student")
    print("2. Read Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        create_student(first_name, last_name, age, grade)
    elif choice == '2':
        read_students()
    elif choice == '3':
        student_id = int(input("Enter Student ID: "))
        grade = input("Enter New Grade: ")
        update_student(student_id, grade)
    elif choice == '4':
        student_id = int(input("Enter Student ID: "))
        delete_student(student_id)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

cursor.close()
connection.close()
