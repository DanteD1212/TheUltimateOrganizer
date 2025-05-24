#Este es el archivo principal

import os
import sys
from core import organizar_archivos

rutabase = ""
while (not os.path.exists(rutabase)):
    print("Si desea salir, escriba s y luego presione Enter")
    rutabase = input("Porfavor introduce la ruta de la carpeta que desear organizar por dentro: ")
    if rutabase == "s":
        sys.exit()
    elif not os.path.exists(rutabase):
        print("La ruta proporcionada no existe, porfavor vuelve a introducir la ruta")
    else:
        break

todoslosarchivos = os.listdir(rutabase)
tam = len(todoslosarchivos)
print(f"\nSe intentarán mover en total {tam} archivos, ¿estás seguro de continuar?")
while True:
    desicion = input("Escriba S/s (Para continuar) o N/n (Para cancelar) y luego presione Enter: ").lower()
    if desicion == "s":
        break
    elif desicion == "n":
        input("Operación cancelada, presione Enter para salir")
        sys.exit()
    else:
        print("Por favor, escriba S para continuar o N para cancelar.")

while True:
    simular = input("¿Deseas ejecutar en modo simulación? (S/N): ").lower()
    if simular in ("s", "n"):
        break
    else:
        print("Por favor, escribe S para sí o N para no.")

modo_simulacion = (simular == "s")
nombre_script = os.path.basename(__file__)

carpetas_creadas, archivos_movidos, archivos_ignorados, errores_al_mover = organizar_archivos(
    rutabase, todoslosarchivos, nombre_script, modo_simulacion
)

print("\nFinalizado!")
if modo_simulacion:
    print("¡Esto fue solo una simulación! No se movió ningún archivo realmente.")
print(f"En total se crearon {carpetas_creadas} carpetas!")
print(f"Total de archivos movidos: {archivos_movidos}")
print(f"Total de archivos que fueron ignorados (por no tener extension, ser carpetas o porque ya existian): {archivos_ignorados}")
print(f"Total de archivos que NO se pudieron mover por permisos: {errores_al_mover}")

print("\n............................")
input("Presiona Enter para salir...")