import matplotlib.pyplot as plt
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]
plt.bar(categorias,valores)
plt.xlabel("Categorias")
plt.ylabel("Valores")
for i, valor in enumerate(valores):
    plt.text(i, valor,str(valor),color="black")
plt.show()