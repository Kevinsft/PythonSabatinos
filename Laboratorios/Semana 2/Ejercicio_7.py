n = input("Ingrese una lista de numeros separados por coma: ")
suma = 0
ns = [int(i) for i in n.split(",")]
for i in ns:
    suma = suma + i
    
print(f"La suma de los numeros es: {suma}")