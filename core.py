#Logica principal de organizacion

import os
import shutil as shu
from categorias import organizacion
from utils import crear_carpeta

def organizar_archivos(rutabase, todoslosarchivos, nombre_script, modo_simulacion):
    carpetas_creadas = 0
    archivos_ignorados = 0
    archivos_movidos = 0
    errores_al_mover = 0

    carpetas_necesarias = set()
    subcarpetas_necesarias = set()

    for archivo in todoslosarchivos:
        if archivo == nombre_script:
            continue
        carpeta_origen = os.path.join(rutabase, archivo)
        if not os.path.isdir(carpeta_origen):
            _, extension = os.path.splitext(archivo)
            if extension == "":
                continue
            categoria = organizacion.get(extension, "otros")
            carpetas_necesarias.add(categoria)
            subcarpetas_necesarias.add((categoria, extension.lstrip(".")))

    for categoria in carpetas_necesarias:
        if crear_carpeta(categoria, rutabase, modo_simulacion):
            carpetas_creadas += 1
    for categoria, subcarpeta in subcarpetas_necesarias:
        ruta_categoria = os.path.join(rutabase, categoria)
        if crear_carpeta(subcarpeta, ruta_categoria, modo_simulacion):
            carpetas_creadas += 1

    for archivo in todoslosarchivos:
        if archivo == nombre_script:
            continue
        carpeta_origen = os.path.join(rutabase, archivo)
        if not os.path.isdir(carpeta_origen):
            nombre, extension = os.path.splitext(archivo)
            if extension == "":
                print(f"El archivo '{archivo}' no tiene extensión, se ignorará.")
                archivos_ignorados += 1
                continue

            carpeta_destino = os.path.join(rutabase, organizacion.get(extension, "otros"))
            carpeta_destino = os.path.join(carpeta_destino, extension.lstrip("."))

            if modo_simulacion:
                print(f"[SIMULACIÓN] Se movería: '{archivo}' → '{carpeta_destino}'")
                archivos_movidos += 1
                continue

            try:
                shu.move(carpeta_origen, carpeta_destino)
                archivos_movidos += 1
            except shu.SameFileError:
                print(f"El archivo {archivo} ya existe en la carpeta destino, asi que no se movera para evitar errores :D")
                archivos_ignorados += 1
            except PermissionError:
                print(f"No tienes permisos para mover el archivo {archivo}.")
                errores_al_mover += 1
        else:
            print(f"La carpeta {archivo} es una carpeta, por lo tanto no se movera")
            archivos_ignorados += 1

    return carpetas_creadas, archivos_movidos, archivos_ignorados, errores_al_mover