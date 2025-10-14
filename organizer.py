"""Script principal para organizar archivos en carpetas por categoría."""

from __future__ import annotations

import os
import sys

from core import organizar_archivos


def solicitar_ruta() -> str:
    """Solicita al usuario una ruta válida y existente."""

    while True:
        print("Si desea salir, escriba s y luego presione Enter")
        ruta = input("Por favor, introduce la ruta de la carpeta que deseas organizar: ")
        if ruta.lower() == "s":
            sys.exit()
        if os.path.exists(ruta):
            return ruta
        print("La ruta proporcionada no existe, por favor vuelve a intentarlo.\n")


def confirmar_accion(mensaje: str) -> bool:
    """Solicita confirmación al usuario para continuar con la acción."""

    while True:
        decision = input(f"{mensaje} (S/N): ").strip().lower()
        if decision in {"s", "n"}:
            return decision == "s"
        print("Por favor, escribe S para continuar o N para cancelar.\n")


def preguntar_simulacion() -> bool:
    """Pregunta si se desea ejecutar en modo simulación."""

    return confirmar_accion("¿Deseas ejecutar en modo simulación?")


def mostrar_resumen(
    modo_simulacion: bool,
    carpetas_creadas: int,
    archivos_movidos: int,
    archivos_ignorados: int,
    errores_al_mover: int,
) -> None:
    """Muestra un resumen de la ejecución del programa."""

    print("\n¡Finalizado!")
    if modo_simulacion:
        print("¡Esto fue solo una simulación! No se movió ningún archivo realmente.")
    print(f"En total se crearon {carpetas_creadas} carpetas.")
    print(f"Total de archivos movidos: {archivos_movidos}")
    print(
        "Total de archivos que fueron ignorados (sin extensión, carpetas o duplicados):"
        f" {archivos_ignorados}"
    )
    print(f"Total de archivos que no se pudieron mover por permisos: {errores_al_mover}")


def main() -> None:
    ruta_base = solicitar_ruta()
    archivos = os.listdir(ruta_base)
    cantidad_archivos = len(archivos)

    if cantidad_archivos == 0:
        print("La carpeta está vacía, no hay archivos para organizar.")
        return

    print(f"\nSe intentarán mover en total {cantidad_archivos} archivos, ¿estás seguro de continuar?")
    if not confirmar_accion("Escribe S para continuar o N para cancelar"):
        input("Operación cancelada, presiona Enter para salir...")
        return

    modo_simulacion = preguntar_simulacion()
    nombre_script = os.path.basename(__file__)

    (
        carpetas_creadas,
        archivos_movidos,
        archivos_ignorados,
        errores_al_mover,
    ) = organizar_archivos(ruta_base, archivos, nombre_script, modo_simulacion)

    mostrar_resumen(
        modo_simulacion,
        carpetas_creadas,
        archivos_movidos,
        archivos_ignorados,
        errores_al_mover,
    )

    print("\n............................")
    input("Presiona Enter para salir...")


if __name__ == "__main__":
    main()
