def buscar_matriz(matriz, elemento):
    for columna, fila in enumerate(matriz):
        if elemento in fila:
            print(f"Su elemento se encuentra en la columna: {columna + 1}, fila {int(fila.index(elemento)) + 1}")
            
            
            
m1 = [[1,2,3],[0,5,6],[7,8,9]]
m2 = [[6,4,1],[0,8,4],[1,1,1]]
buscar_matriz(m1, 0)
buscar_matriz(m2, 4)