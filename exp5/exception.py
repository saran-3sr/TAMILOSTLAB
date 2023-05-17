# try:
#     age=int(input("Enter your age: "))
#     if(age>=18 and age<=100):
#         print("This is a valid age.")
# except(age<=0 and age>=100) :
#     print("Out of bounds error for age")
# except(age>0 and age<=17):
#     print("underaged : age is not sufficient")

class InvalidageException(Exception):
    pass
class OutofBoundException(Exception):
   pass


try:
    age=int(input("Enter your age: "))
    if(age>=18 and age<=100):
        print("This is a valid age.")
    elif(age>0 and age <=17):
        raise InvalidageException
    else:
        raise OutofBoundException
except InvalidageException:
    print("underaged : age is less than 18 not eligible to vote")
except OutofBoundException:
    print("Age is out of bound")

# class OutofBoundage(Exception):

#     def __init__(self, age, message="Age is out of bound"):
#         self.age = age
#         self.message = message
#         super().__init__(self.message)

# class InvalidageException(Exception):

#     def __init__(self, age, message="Age is invalid"):
#         self.age = age
#         self.message = message
#         super().__init__(self.message)

# age = int(input("Enter your age: "))
# if age<0 and age>100:
#     raise OutofBoundage(age)
# elif age>=0 and age<=17:
#     raise InvalidageException(age)
# else:
#     print("The age is valid")