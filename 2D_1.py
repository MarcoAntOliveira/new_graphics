import matplotlib.pyplot as plt 
import numpy as np
 
x = np.arange(1, 20)
y = 3*x - 3
z = x**2 + 1
w = 2*x**2 - 3

plt.subplot(311);plt.plot(x, y)
plt.subplot(312);plt.plot(x, z)
plt.subplot(313);plt.plot(x, w);plt.show()
