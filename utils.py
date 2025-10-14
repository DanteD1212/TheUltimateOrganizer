"""Funciones auxiliares para la organización de archivos."""

from __future__ import annotations

import os


def crear_carpeta(nombre_carpeta: str, ruta_base: str, modo_simulacion: bool) -> bool:
    """Crea una carpeta y devuelve True si se creó.

    Si la carpeta ya existe se devuelve False. En modo simulación no se crea
    realmente la carpeta, pero se indica como creada para conservar el flujo
    del programa original.
    """

    ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)
    if os.path.exists(ruta_carpeta):
        return False

    if not modo_simulacion:
        os.makedirs(ruta_carpeta)

    return True
