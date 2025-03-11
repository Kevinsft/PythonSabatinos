texto = input("Ingrese el texto que desea cifrar: ").lower()
n = int(input("Ingrese cuantos desplazamientos tendra el cifrado: "))

abc = "abcdefghijklmnñopqrstuvwxyz"
def cifrado_cesar(t, n):
    txtCifrado = ""
    for i in t:
        suma = abc.find(i) + n
        modulo = int(suma) % len(abc)
        txtCifrado = txtCifrado + str(abc[modulo])
    return txtCifrado

print(cifrado_cesar(texto, n))