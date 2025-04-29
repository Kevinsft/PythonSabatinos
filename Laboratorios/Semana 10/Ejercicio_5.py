import openpyxl
book = openpyxl.load_workbook("mi_libro.xlsx")
sheet = book.active
sheet["D1"] = "Total"
sheet["D2"] = "=B2*C2"
sheet["D3"] = "=B3*C3"
book.save("mi_libro.xlsx")
print("Archivo modificado")