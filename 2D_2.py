import matplotlib.pyplot as plt
import numpy as np
lista1 =[1, 2, 3, 2, 4, 5, 3, 2, 1, 2, 3, 4, 5]
lista2 =[-1, -2, -1, 0, 1, 2, 3, 2, 1, -1, -2]
lista3 =[10, 9, 8, 7, 9, 11, 14]
lista4 =[100, 101, 102, 100, 99, 98, 99, 100]

plt.subplot(221);plt.plot(lista1)
plt.subplot(222);plt.plot(lista2)
plt.subplot(223);plt.plot(lista3)
plt.subplot(224);plt.plot(lista4);plt.show()
