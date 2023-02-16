import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
eixos = fig.add_subplot(projection = '3D')
x,y,z =  axes3d.get_test_data(0.10)

eixos.plot_wireframe(x,y,z)
plt.show()