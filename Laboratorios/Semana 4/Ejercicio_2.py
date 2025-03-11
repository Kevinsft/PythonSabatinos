def Invertir_Cadena(Cadena):
    cInvertida = ""
    txtInvertido = ""
    for i in Cadena:
        if i == " ":
            txtInvertido = txtInvertido + " " + cInvertida
            cInvertida = ""
        else:
            cInvertida = i + cInvertida
    txtInvertido = txtInvertido + " " + cInvertida
    return txtInvertido

texto = input("Introduce el texto: ")
print(Invertir_Cadena(texto))