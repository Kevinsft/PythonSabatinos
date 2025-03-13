def suma_matrices(a,b):
    if len(a) != len(b):
        print("Las 2 matrices deben ser 3x3")
    elif len(a[0]) != len(b[0]):
        print("Las 2 matrices deben ser 3x3")
    else:
        matriz_sresultante = []
        for i in range(len(a)):
            fila = []
            for j in range(len(a[0])):
                fila.append(a[i][j] + b[i][j])
            matriz_sresultante.append(fila)
        return matriz_sresultante
    
m1 = [[1,2,3],[0,5,6],[6,3,1]]
m2 = [[6,4,1],[0,8,4],[1,1,1]]

print(f"Suma de matices: {suma_matrices(m1,m2)}")