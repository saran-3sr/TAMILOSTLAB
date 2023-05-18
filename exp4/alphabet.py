import string
alphabets =list(string.ascii_uppercase)
f=open('file1.txt','w')
f1=open('file1.txt','r')
a=0
for i in alphabets:
    if(a%3==0):
        f.write("\n")
    f.write(i)
    a+=1
f.close()
print(f1.read())
