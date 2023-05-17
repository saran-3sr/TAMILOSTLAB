import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=a+b
sum_al=np.transpose(a)
sum_b=np.transpose(b)
print(sum_al,sum_b)
# change the function for all operations
# for calculating on axis basic (column or row)use axis parameter in sum function