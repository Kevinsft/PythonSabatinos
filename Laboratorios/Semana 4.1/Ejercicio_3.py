def producto_punto(v1,v2):
    if len(v1) != len(v2):
        print("Los vectores deben tener la misma longitud")
    else:
        resultado = 0
        for i in range(len(v1)):
            resultado += int(v1[i]*v2[i])
        return resultado
    
vector1 = [-3,5,5]
vector2 = [2,-4,8]
print(producto_punto(vector1,vector2))