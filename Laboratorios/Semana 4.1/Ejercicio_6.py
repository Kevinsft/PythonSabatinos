def suma_diagonales(m):
    principal = 0
    secundaria = 0
    j = -1
    for i in range(len(m)):
        principal += m[i][i]
    for h in range(len(m)):
        secundaria += m[h][j]
        j -= 1
    return principal, secundaria

m1 = [[1,2,3,4,5],[0,5,6,8,1],[7,8,9,4,4],[8,4,5,2,0],[0,0,1,0,0]]
print(suma_diagonales(m1))