n1 = int(input("Ingrese un numero entre 1 al 20: "))
while n1 < 1 or n1 > 20:
    n1 = int(input("Ingrese un numero entre 1 al 20: "))
    
Factorial = n1
i = n1
while i > 0:
    if i - 1 != 0:
        Factorial = Factorial * (i-1)
    i = i - 1
    
print(f"El factorial de {n1} es {Factorial}")