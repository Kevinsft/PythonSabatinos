def matriz_transpuesta(m):
    transpuesta = list(zip(*m))
    return transpuesta

m1 = [[1,2,3],[0,5,6],[6,3,1]]
m2 = [[6,4,1],[0,8,4],[1,1,1]]
print(matriz_transpuesta(m1))
print(matriz_transpuesta(m2))