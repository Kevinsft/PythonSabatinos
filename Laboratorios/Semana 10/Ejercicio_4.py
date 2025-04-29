import openpyxl
book = openpyxl.load_workbook("mi_libro.xlsx")
sheet = book.active
sheet["C2"] = 0.55
book.save("mi_libro.xlsx")
print("Archivo modificado")