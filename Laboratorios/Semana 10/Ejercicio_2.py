import openpyxl
book = openpyxl.Workbook()
sheet = book.active
sheet.title = "Ventas"
datos = [
    ["Producto", "Cantidad", "Precio"],
    ["Manzanas", 50, 0.5],
    ["Naranjas", 30, 0.75]
]
for i in datos:
    sheet.append(i)
book.save("mi_libro.xlsx")