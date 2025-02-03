n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))

if n1 == n2:
    print("Los numeros son iguales")
elif n1 > n2:
    print(f"{n1} es mayor a {n2}")
else:
    print(f"{n1} es menor a {n2}")