calc = {
        "add" : lambda a, b: a + b,
        "sub" : lambda a, b: a - b,
        "mul" : lambda a, b: a * b,
        "div" : lambda a, b: a / b,
        }
a = float(input("Enter num1: "))
b = float(input("Enter num2: "))
op = input("Enter operation: ")
print(calc[op](a, b))
