palabras = input("Ingrese una lista de palabras separadas por un espacio: ")
lista_palabras = palabras.split()
lista_ordenada_longitud = sorted(lista_palabras, key=len)

print(lista_ordenada_longitud)