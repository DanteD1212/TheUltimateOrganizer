"""Lógica principal para organizar los archivos dentro de una carpeta."""

from __future__ import annotations

import os
import shutil
from typing import Iterable, Tuple

from categorias import organizacion
from utils import crear_carpeta


def _obtener_extension(archivo: str) -> str:
    """Obtiene la extensión del archivo en minúsculas."""

    _, extension = os.path.splitext(archivo)
    return extension.lower()


def organizar_archivos(
    ruta_base: str, archivos: Iterable[str], nombre_script: str, modo_simulacion: bool
) -> Tuple[int, int, int, int]:
    """Organiza los archivos según la tabla de categorías."""

    carpetas_creadas = 0
    archivos_ignorados = 0
    archivos_movidos = 0
    errores_al_mover = 0

    carpetas_necesarias = set()
    subcarpetas_necesarias = set()

    for archivo in archivos:
        if archivo == nombre_script:
            continue

        ruta_archivo = os.path.join(ruta_base, archivo)
        if not os.path.isfile(ruta_archivo):
            continue

        extension = _obtener_extension(archivo)
        if not extension:
            continue

        categoria = organizacion.get(extension, "otros")
        carpetas_necesarias.add(categoria)
        subcarpetas_necesarias.add((categoria, extension.lstrip(".")))

    for categoria in carpetas_necesarias:
        if crear_carpeta(categoria, ruta_base, modo_simulacion):
            carpetas_creadas += 1

    for categoria, subcarpeta in subcarpetas_necesarias:
        ruta_categoria = os.path.join(ruta_base, categoria)
        if crear_carpeta(subcarpeta, ruta_categoria, modo_simulacion):
            carpetas_creadas += 1

    for archivo in archivos:
        if archivo == nombre_script:
            continue

        ruta_origen = os.path.join(ruta_base, archivo)
        if not os.path.isfile(ruta_origen):
            print(f"La carpeta '{archivo}' es una carpeta, por lo tanto no se moverá.")
            archivos_ignorados += 1
            continue

        extension = _obtener_extension(archivo)
        if not extension:
            print(f"El archivo '{archivo}' no tiene extensión, se ignorará.")
            archivos_ignorados += 1
            continue

        categoria = organizacion.get(extension, "otros")
        carpeta_categoria = os.path.join(ruta_base, categoria)
        carpeta_destino = os.path.join(carpeta_categoria, extension.lstrip("."))

        if modo_simulacion:
            print(f"[SIMULACIÓN] Se movería: '{archivo}' → '{carpeta_destino}'")
            archivos_movidos += 1
            continue

        try:
            shutil.move(ruta_origen, carpeta_destino)
            archivos_movidos += 1
        except shutil.SameFileError:
            print(
                "El archivo '%s' ya existe en la carpeta destino, así que no se moverá"
                " para evitar errores."
                % archivo
            )
            archivos_ignorados += 1
        except PermissionError:
            print(f"No tienes permisos para mover el archivo '{archivo}'.")
            errores_al_mover += 1

    return carpetas_creadas, archivos_movidos, archivos_ignorados, errores_al_mover
