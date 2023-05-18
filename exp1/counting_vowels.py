# str1=input("Enter a string: ")
# vowels=['a','e','i','o','u','A','E','I','O','U']
# # vowels="aeiouAEIOU"
# dict1={}
# for i in vowels:
#     dict1[i]=str1.count(i)
# print(dict1)

s1=input("Enter the string: ")
vow=['a','e','i','o','u']
s1=s1.lower()
count=0
for i in s1:
    if i in vow:
        count=count+1
print("Total Vowels ", count)
