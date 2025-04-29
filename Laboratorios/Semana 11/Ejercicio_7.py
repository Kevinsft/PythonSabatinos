import matplotlib.pyplot as plt
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]
plt.barh(categorias,valores,color="green")
plt.xlabel("Valores")
plt.ylabel("Categorias")
plt.show()