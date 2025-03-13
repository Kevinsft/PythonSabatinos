m = int(input("Ingrese el numero de filas que tendra la matriz: "))
n = int(input("Ingrese el numero de columnas que tendra la matriz: "))

def crear_matriz(m1,n1):
    matriz = []
    for i in range(m1):
        fila = []
        for j in range(n1):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

print(f"Matriz creada: {crear_matriz(m,n)}")