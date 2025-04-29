import matplotlib.pyplot as plt
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]
plt.bar(categorias,valores,color="blue")
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.show()