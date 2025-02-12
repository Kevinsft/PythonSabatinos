cadena = input("Ingrese una cadena de texto: ")
caracter = input("Ingrese el caracter que desea contar: ")
j = 0
for i in cadena:
    if caracter == i:
        j = j + 1
        
print(f"El caracter {caracter}, aparece {j} veces en la cadena de texto")