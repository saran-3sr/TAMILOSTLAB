# num=int(input("Ente the number: "))
# print("The prime numbers till the entered number are: \n")
# for i in range(2,num+1):
#     count=0
#     for j in range(2,i+1):
#         if(i%j==0):
#             count+=1
#     if(count==1):
#         print(i)


num=int(input("Enter the range to check for prime "))
for i in range(1,num+1):
    flag=0
    for j in range(2,int(i/2)):
       if i%j==0:
           flag=1
           break
    if flag==0:
        print(i)
