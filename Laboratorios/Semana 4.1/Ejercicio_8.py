def distancia_entre_puntos(p1,p2):
    distancia = (((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**(1/2)
    return distancia

punto1 = (2,3)
punto2 = (5,7)
print(f"La distancia entre el punto {punto1} y {punto2} es: {distancia_entre_puntos(punto1,punto2)}")