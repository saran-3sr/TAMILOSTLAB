f1=open('sample1.txt','r')
f2=open('sample2.txt','w')

for line in f1:
    f2.write(line)

f2.close()
f1.close()
print("The contents are copied successfully")
