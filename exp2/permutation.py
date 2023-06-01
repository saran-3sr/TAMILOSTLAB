# def permutFunc(myList):
# 	if len(myList) == 0:
# 		return []
# 	if len(myList) == 1:
# 		return [myList]
# 	k = []
# 	for i in range(len(myList)):
# 		m = myList[i]
# 		res = myList[:i] + myList[i+1:]
# 		for p in permutFunc(res):
# 			k.append([m] + p)
# 	return k

# myList = list(input("enter a string: "))
# for p in permutFunc(myList):
# 	print (p)
#permutaion
def permutation(mylist):
  if len(mylist)==0:
    return
  elif len(mylist)==1 :
    return mylist
  k=[]
  for i in range(len(mylist)):
    m=mylist[i]
    for p in permutation(mylist[:i]+mylist[i+1:]):
        k.append(m+p)
  return k

mylist = list(input("enter a string: "))
for p in permutation(mylist):
	l1=list(p)
	print(l1)
