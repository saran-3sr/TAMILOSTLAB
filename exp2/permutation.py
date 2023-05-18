def permutFunc(myList):
	if len(myList) == 0:
		return []
	if len(myList) == 1:
		return [myList]
	k = []
	for i in range(len(myList)):
		m = myList[i]
		res = myList[:i] + myList[i+1:]
		# print("x: ",res)
		for p in permutFunc(res):
			k.append([m] + p)
	return k

myList = list(input("enter a string: "))
for p in permutFunc(myList):
	print (p)