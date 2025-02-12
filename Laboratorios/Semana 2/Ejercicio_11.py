n = input("Ingrese un numero: ")
numeros = [int(i) for i in n]
ds = 0
for j in numeros:
    ds = ds + j

print (f"La suma de sus digitos es: {ds}")