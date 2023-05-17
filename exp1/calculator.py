num1=int(input('Enter a number: '))
num2=int(input("enter another number: "))
while 1:
    ch=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter your choice: "))
    if(ch==1):
        res=num1+num2
    elif(ch==2):
        res=num1-num2
    elif(ch==3):
        res=num1*num2
    elif(ch==4):
        res=num1/num2
    else:
        break
    print("Result: ",res)