numeros = input("Ingrese una lista de numeros separados por un espacio: ")
listaN = numeros.split()
lista_pares = []
for i in listaN:
    if int(i) % 2 == 0:
        lista_pares.append(i)
        
print(f"Lista con solo los numeros pares: {lista_pares}")