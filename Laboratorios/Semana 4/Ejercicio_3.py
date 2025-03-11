texto = input("Escribe una frase: ")
vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
k = 0
j = 0
for i in texto:
    if i in vocales:
        j = j + 1
for h in texto:
    if h in consonantes:
        k += 1
        
print(f"La frase {texto}, tiene {j} vocales y {k} consonantes")