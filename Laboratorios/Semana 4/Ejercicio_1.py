texto = input("Introduzca el texto: ")
contador = 1
for i in texto:
    if i == " ":
        contador += 1
    
print(f"Tu texto tiene {contador} palabras")

#O tambien
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

parrafo = """Este es un ejemplo de párrafo largo. El programa contará cuántas palabras contiene este texto."""
resultado = contar_palabras(parrafo)
print(f"El texto contiene {resultado} palabras.")