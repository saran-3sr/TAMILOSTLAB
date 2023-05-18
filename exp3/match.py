dict1={1:'apple',2:'orange',3:'jackfruit'}
dict2={3:'jackfruit',4:'peach',5:'guava'}

for i in dict1:
   for j in dict2:
      if(dict1[i]==dict2[j] and i==j):
         print( "key ",i,"  with value ",dict1[i],"is identical in both dictionaries")
   