import math
def conversion_coordenadas(r,o):
    x = math.cos(r)
    y = math.sin(o)
    return (x, y)

p1 = 5
p2 = math.radians(45)
print(conversion_coordenadas(p1,p2))