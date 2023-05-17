string=(input("Enter a string: "))
string1=string.split()
print("enter two strings to replace: ")
str1=input()
str2=input()
for i in range(0,len(string1)):
    if(string1[i]==str2):
       string1[i]=str1
    elif(string1[i]==str1):
        string1[i]=str2
print("after replacing: \n")
print(' '.join(string1))
