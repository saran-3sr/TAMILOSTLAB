dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6}

key = input("Enter a key: ")

if key in dict1 and key in dict2:
    print("The key is in both dictionaries.")
elif key in dict1:
    print("The key is in the first dictionary.")
elif key in dict2:
    print("The key is in the second dictionary.")
else:
    print("The key is in none of the dictionaries.")
