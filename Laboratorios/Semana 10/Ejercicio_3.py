import openpyxl
book = openpyxl.load_workbook("mi_libro.xlsx")
sheet = book.active
datos = []
for i in sheet.iter_rows(values_only = True):
    datos.append(list(i))
print(datos)