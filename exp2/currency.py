cur_list=[2000,500,200,100,50,20,10,5,2,1]
amount=int(input("Enter the amount: "))
                                    
for i in cur_list:
    count=0
    while(amount>=i):
        amount-=i
        count+=1
    if(count>0):
        print(i,"-->",count)