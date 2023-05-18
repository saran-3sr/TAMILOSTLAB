import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,200)
y=np.cos(x)
plt.plot(x,y)
plt.xlabel("Degree")
plt.ylabel("value- Y")
plt.title("Cos Curve")
plt.show()