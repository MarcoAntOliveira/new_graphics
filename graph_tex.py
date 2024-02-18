import matplotlib.pyplot as plt

# Dados para plotagem
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Plotagem
plt.plot(x, y)
plt.xlabel(r'$\iint$', fontsize=16)  # Expressão LaTeX dentro do rótulo do eixo x
plt.ylabel(r'$\beta$', fontsize=16)   # Expressão LaTeX dentro do rótulo do eixo y
plt.title(r'$\int$ vs. $\beta$', fontsize=20)  # Título do gráfico em LaTeX
plt.grid(True)
plt.show()
