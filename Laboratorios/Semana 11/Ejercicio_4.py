import sympy
x = sympy.symbols("x")
f = sympy.Function("f")
fx = x**2 + 3*x + 2
ln = float(input("Ingrese un numero flotante: "))
limite = sympy.limit(fx / ln, x, 0)
derivada = sympy.diff(fx, x)
print(f"Funcion: {fx}")
print(f"Limite: {limite}")
print(f"Derivada: {derivada}")