tuple1 = tuple(map(int, input("Enter the elements of the first tuple, separated by spaces: ").split()))
tuple2 = tuple(map(int, input("Enter the elements of the second tuple, separated by spaces: ").split()))

sum1 = sum(tuple1)
sum2 = sum(tuple2)

print("Sum of elements in the first tuple: ", sum1)
print("Sum of elements in the second tuple: ", sum2)
