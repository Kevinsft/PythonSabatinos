p = input("Ingrese una lista de plabras: ")
ps = []
for i in p.split(" "):
    ps.append(i)

cantidadP = len(ps) 
print(f"La cantidad de palabras es: {cantidadP}")