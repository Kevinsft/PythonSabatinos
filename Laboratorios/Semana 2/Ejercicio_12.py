lista = []
n = int(input("Ingrese la cantidad de numeros que tendra la lista: "))

i = 1
while i <= n:
    nl = int(input("Ingrese un numero: "))
    lista.append(nl)
    i += 1
    
print(f"Lista de numeros: {lista}")
lista.sort()
print(f"Lista ordenada: {lista}")