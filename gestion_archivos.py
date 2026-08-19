import json 
import os 
carpeta_reportes ="reports"
ruta_archivo = os.path.join(carpeta_reportes, "reparaciones.json")
def guardar_reparaciones(lista_reparaciones):
    if not os.path.exists(carpeta_reportes):
        os.makedirs(carpeta_reportes)
    with open(ruta_archivo, "w", encoding='utf-8') as archivo_json:
        json.dump(lista_reparaciones, archivo_json, indent=4)
def cargar_reparaciones():
    if not os.path.exists(ruta_archivo):
        return[]
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_json:
            return json.load(archivo_json)
    except Exception:
        return []