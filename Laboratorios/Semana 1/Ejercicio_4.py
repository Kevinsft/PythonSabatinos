n1 = int(input("Ingresa tu edad: "))

if n1 <= 12:
    print("Eres niño")
elif (n1 > 12) & (n1 < 18):
    print("Eres adolescente")
elif (n1 >= 18) & (n1 < 60):
    print("Eres un adulto")
elif (n1 >= 60) & (n1 < 110):
    print("Eres un adulto mayor")
else:
    print("¿Como puedes tener tantos años?")