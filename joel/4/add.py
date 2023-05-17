num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print("Data type of num1: ", type(num1))
print("Data type of num2: ", type(num2))

num1 = int(num1)
num2 = int(num2)

print("Data type of num1 after casting to int: ", type(num1))
print("Data type of num2 after casting to int: ", type(num2))

num1 = str(num1)
num2 = str(num2)

print("Data type of num1 after casting to string: ", type(num1))
print("Data type of num2 after casting to string: ", type(num2))

print("Result: num1 = ", num1, ", num2 = ", num2)
