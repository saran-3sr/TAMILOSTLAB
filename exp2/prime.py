num=int(input("Ente the number: "))
print("The prime numbers till the entered number are: \n")
for i in range(2,num+1):
    count=0
    for j in range(2,i+1):
        if(i%j==0):
            count+=1
    if(count==1):
        print(i)