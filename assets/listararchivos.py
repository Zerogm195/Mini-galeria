import os
import json

# Obtener el directorio donde está el script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

#Cambiar directorio hacia el cual quiere obtener la lista de imagenes
carpeta = "C:/Users/luisd/OneDrive/Documentos/web/Mini galeria/assets/img"

# Usar os.path.join para crear la ruta al archivo data.json
ruta_json = os.path.join(directorio_actual, "data.json")

def obtenerDatos():
    archivos = [f for f in os.listdir(carpeta)]

    imagenes =[]

    for archivo in archivos:
        imagenes.append(archivo)

    datos = {"imagenes" : imagenes}

    #print(datos["imagenes"]) #ver datos en la lista datos

    with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

obtenerDatos()