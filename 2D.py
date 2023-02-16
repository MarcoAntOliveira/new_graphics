import matplotlib.pyplot as plt
import numpy as np
x = np.arange (1, 20)
y = 3*x - 3

plt.title('meu primerio grafico')

plt.plot(x, y);plt.plot('x');plt.ylabel('y')
plt.grid()


plt.show() 