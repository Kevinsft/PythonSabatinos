import openpyxl
book = openpyxl.Workbook()
sheet = book.active
sheet2 = book.create_sheet("Datos")
book.save("mi_libro.xlsx")