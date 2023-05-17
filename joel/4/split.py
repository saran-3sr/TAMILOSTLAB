import string

num = int(input())
alpha = string.ascii_lowercase

for i in range(0, len(alpha), num):
    print(alpha[i:i+num])
