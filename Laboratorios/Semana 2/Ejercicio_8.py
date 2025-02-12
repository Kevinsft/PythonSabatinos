lista = []
n = int(input("Ingrese la cantidad de numeros que tendra la lista: "))

i = 1
while i <= n:
    nl = int(input("Ingrese un numero: "))
    lista.append(nl)
    i += 1
    
print("Numero mayor de la lista: ", max(lista))
print("Numero menor de la lista: ", min(lista))