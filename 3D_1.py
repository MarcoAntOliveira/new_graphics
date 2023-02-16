import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection= '3d')

def f(x, y):
    return x**2 + y**2
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax = plt.axes(projection = '3d')
ax.plot_wireframe(X, Y, Z, color = 'aqua')
ax.set_title('titulo')
plt.show()
