texto = input("Escribe una frase: ")
vocales = "aeiouAEIOU"

j = 0
for i in texto:
    if i in vocales:
        j = j + 1
        
print(f"La frase {texto}, tiene {j} vocales")