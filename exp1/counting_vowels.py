str1=input("Enter a string: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
# vowels="aeiouAEIOU"
dict1={}
for i in vowels:
    dict1[i]=str1.count(i)
print(dict1)