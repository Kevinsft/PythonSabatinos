Suma_Impares = 0
for i in range(2,101):
    if i % 2 == 0:
        Suma_Impares = Suma_Impares + i
        print(Suma_Impares)

print(f"La suma de impares es: {Suma_Impares}")