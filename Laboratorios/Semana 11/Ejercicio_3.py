import statistics
numeros = input("Ingrese 25 numeros enteros separados por coma: ")
lista_numeros = numeros.split(",")
lista_numeros = [int(num) for num in lista_numeros]
media = statistics.mean(lista_numeros)
mediana = statistics.median(lista_numeros)
moda = statistics.mode(lista_numeros)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")