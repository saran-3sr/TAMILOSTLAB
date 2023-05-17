def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in input_string if char in vowels)

input_string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(input_string))
