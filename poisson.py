import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

k = np.linspace(0, 100, 101)

lambda1 = 5
lambda2 = 20
lambda3 = 50
lambda4 = 80

f1 = []
f2 = []
f3 = []
f4 = []

for i in range(len(k)):
    f1.append(((lambda1**int(k[i]))*np.exp(-1.0*lambda1))/math.factorial(int((k[i]))))
    f2.append(((lambda2**int(k[i]))*np.exp(-1.0*lambda2))/math.factorial(int(k[i])))
    f3.append(((lambda3**int(k[i]))*np.exp(-1.0*lambda3))/math.factorial(int(k[i])))
    f4.append(((lambda4**int(k[i]))*np.exp(-1.0*lambda4))/math.factorial(int(k[i])))
    
plt.plot(k, f1, label=r'$\lambda$=5')
plt.plot(k, f2, label=r'$\lambda$=20')
plt.plot(k, f3, label=r'$\lambda$=50')
plt.plot(k, f4, label=r'$\lambda$=80')  
plt.xlabel('k')
plt.ylabel('p(x=k)')
plt.legend()
plt.tight_layout()
plt.show()