import requests
url = "https://swapi.dev/api/people/"
personajes = []
respuesta = requests.get(url)
if respuesta.status_code == 200:
    datos = respuesta.json()
    personaje = respuesta["results"]
    for p in personaje:
        if personaje["name"].startswith("L"):
            personajes.append({"name" : personaje["name"], "height" : personaje["height"]})     
    for i in personajes:
        print(f"Nombre: {i["name"]}, altura: {i["height"]}")
else:
    print("ERROR")