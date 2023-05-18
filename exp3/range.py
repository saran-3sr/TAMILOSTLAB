list1=[i for i in range(1,31)]
print(list1)
list2=[]
list3=[]
for i in range(0,5):
    list2.append(list1[i]*list1[i])
for i in range(-5,0):
    list3.append(list1[i]*list1[i])
print("The first 5 square of elements is \n",list2,"\n")
print("The last 5 square of elements is \n",list3)
