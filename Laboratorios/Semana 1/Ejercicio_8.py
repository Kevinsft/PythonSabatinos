n1 = int(input("Ingrese el año: "))

if n1%4 == 0:
    if n1%100 == 0 & n1%400 == 0:
        print("Es año bisiesto")
    elif n1%100 == 0:
        print("Es año no bisiesto")
    else:
        print("Es año bisiesto")
else:
    print("Es año no bisiesto")