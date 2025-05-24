#Funciones auxiliares (Crear carpetas, validar direcciones, etc.)
import os

def crear_carpeta(carpetinha, rutabase, modo_simulacion):
    nombre_carpeta = os.path.join(rutabase, carpetinha)
    if not os.path.exists(nombre_carpeta):
        if not modo_simulacion:
            os.makedirs(nombre_carpeta)
        return True
    return False