import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,11)
y=2*x+5
plt.title("Line Plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y)
plt.show()
