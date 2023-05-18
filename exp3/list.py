list1=[]
print("Choose the data type: \n1.int\n2.float\n3.boolean\n4.string\n")
while 1:
    ch=int(input("Enter your choice: "))
    if(ch==1):
        x=int(input("enter an integer: "))
        list1.append(x)
    elif(ch==2):
        x=float(input("enter a float value: "))
        list1.append(x)
    elif(ch==3):
        x=bool(input("enter a boolean value: "))
        list1.append(x)
    elif(ch==4):
        x=(input("enter a string: "))
        list1.append(x)
    else:
        break
print(list1)