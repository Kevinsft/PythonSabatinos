NombreCompleto = input("Introduce tu nombre completo: ")

def iniciales(Nombre):
    ini = []
    inicialesN = ""
    for i in Nombre:
        if i != " ":
            ini.append(i)
        else:
            inicialesN = inicialesN + str(ini[0])
            ini.clear()
    inicialesN = inicialesN + str(ini[0])
    return inicialesN.upper()

print(iniciales(NombreCompleto))