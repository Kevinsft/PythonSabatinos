n1 = float(input("Ingrese el precio del producto: "))
n2 = int(input("Ingrese el descuento: "))

descuento = (n2*100) / n1
Precion_Final = n1 - descuento
print(f"El precio con el descuento es: {Precion_Final}")