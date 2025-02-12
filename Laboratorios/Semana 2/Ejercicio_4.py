n = int(input("Ingrese un numero entre 1 y 50: "))

while n < 1 or n > 50:
    n = int(input("Ingrese un numero entre 1 y 50: "))
    
a = 0
b = 1

if n == 1:
    print(a)
elif n == 2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(n - 2):
        c = a+b
        a = b
        b = c
        print(b)