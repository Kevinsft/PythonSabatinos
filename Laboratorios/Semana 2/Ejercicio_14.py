from random import randint
n = int(input("Ingrese la cantidad de numeros que desea generar entre 1 y 100: "))
while n < 1 or n > 100:
    n = int(input("Ingrese la cantidad de numeros que desea generar entre 1 y 100: "))

i = 1  
while i <= n:
    print(randint(1, 1000))
    i += 1