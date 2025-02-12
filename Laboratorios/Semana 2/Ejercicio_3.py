np = int(input("Ingrese un numero: "))

i = 0
if np <= 1:
    print(f"El numero {np}, no es un numero primo")
elif np == 2:
    print(f"El numero {np}, es un numero primo")
else:
    for j in range(2,np):
        if np % j == 0:
            i = 1
    if i == 0:
        print(f"El numero {np}, es un numero primo")
    else:
        print(f"El numero {np}, no es un numero primo")