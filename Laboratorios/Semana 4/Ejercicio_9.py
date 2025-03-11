l1 = input("Ingrese los elementos de la primera lista separados por un espacio: ")
l2 = input("Ingrese los elementos de la segunda lista separados por un espacio: ")
lista1 = l1.split()
lista2 = l2.split()
lista1.sort()
lista2.sort()
lista3 = lista1 + lista2
lista3.sort()
print(f"Listas combinadas ordenadas: {lista3}")