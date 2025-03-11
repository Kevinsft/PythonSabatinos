txt1 = input("Ingrese una cadena: ")
txt2 = input("Ingrese una subcadena: ")

def txtC(t1, t2):
    contador = 0
    if t2 in t1:
        contador += 1
    print(f"La subcadena {t2} aparece {contador} veces en la cadena {t1}")

txtC(txt1, txt2)