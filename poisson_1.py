from scipy.stats import poisson
import seaborn as sns
import matplotlib.pyplot as plt

dados_poisson =poisson.rvs(mu = 5, size = 100)
sns.displot(dados_poisson)
plt.xlim(0, 15)
plt.xlabel('k')
plt.ylabel('p(x=k)')
plt.show()