import os
import sys
import shutil as shu

rutabase = ""

# Eleccion de la ruta base (cosas del usuario)
while (not os.path.exists(rutabase)):
    print("Si desea salir, escriba s y luego presione Enter")
    rutabase = input("Porfavor introduce la ruta de la carpeta que desear organizar por dentro: ")
    if rutabase == "s":
        sys.exit()
    elif not os.path.exists(rutabase):
        print("La ruta proporcionada no existe, porfavor vuelve a introducir la ruta")
    else:
        break



todoslosarchivos = os.listdir(rutabase) #Lista de archivos y carpetas dentro de la carpeta_origen
tam = len(todoslosarchivos)
print(f"Se intentarán mover en total {tam} archivos, ¿estás seguro de continuar?")
while True:
    desicion = input("Escriba S/s (Para continuar) o N/n (Para cancelar) y luego presione Enter: ").lower()
    if desicion == "s":
        break
    elif desicion == "n":
        input("Operación cancelada, presione Enter para salir")
        sys.exit()
    else:
        print("Por favor, escriba S para continuar o N para cancelar.")





global carpetas_creadas
carpetas_creadas=0
archivos_ignorados = 0
archivos_movidos = 0
errores_al_mover = 0
nombre_script = os.path.basename(__file__)

#Funcion para crear carpetas
def crear_carpeta(carpetinha, rutabase):
    global carpetas_creadas
    nombre_carpeta = os.path.join(rutabase, carpetinha) #Por ejemplo si nombre_carpeta es imagenes, creara la carpeta_origen C:/Users/issac/Desktop/THEorganizer/imagenes
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
        carpetas_creadas += 1
        #print(f"La carpeta {carpetinha} ha sido creada exitosamente!") para debugear, favor de ignorar

organizacion = {
    # Imagenes
    ".png": "imagenes",
    ".jpg": "imagenes",
    ".jpeg": "imagenes",
    ".gif": "imagenes",
    ".bmp": "imagenes",
    ".tiff": "imagenes",
    ".svg": "imagenes",
    ".ico": "imagenes",
    ".drawio": "imagenes",
    ".webp": "imagenes",
    ".psd": "imagenes",
    ".heic": "imagenes",

    # Codigos
    ".java": "codigos",
    ".py": "codigos",
    ".c": "codigos",
    ".cu": "codigos",
    ".cpp": "codigos",
    ".js": "codigos",
    ".ts": "codigos",
    ".html": "codigos",
    ".css": "codigos",
    ".php": "codigos",
    ".rb": "codigos",
    ".go": "codigos",
    ".rs": "codigos",
    ".swift": "codigos",
    ".kt": "codigos",
    ".cs": "codigos",
    ".sh": "codigos",
    ".bat": "codigos",
    ".pl": "codigos",
    ".sql": "codigos",
    ".json": "codigos",
    ".xml": "codigos",
    ".yml": "codigos",
    ".yaml": "codigos",

    # Instaladores
    ".msi": "instaladores",
    ".exe": "instaladores",
    ".apk": "instaladores",
    ".deb": "instaladores",
    ".rpm": "instaladores",
    ".pkg": "instaladores",
    ".dmg": "instaladores",

    # Audios
    ".mp3": "audios",
    ".flac": "audios",
    ".wav": "audios",
    ".aac": "audios",
    ".ogg": "audios",
    ".m4a": "audios",
    ".wma": "audios",

    # Videos
    ".mp4": "videos",
    ".mkv": "videos",
    ".avi": "videos",
    ".mov": "videos",
    ".wmv": "videos",
    ".flv": "videos",
    ".webm": "videos",
    ".mpeg": "videos",

    # Documentos
    ".doc": "documentos",
    ".docx": "documentos",
    ".odt": "documentos",
    ".xls": "documentos",
    ".xlsx": "documentos",
    ".ods": "documentos",
    ".ppt": "documentos",
    ".pptx": "documentos",
    ".odp": "documentos",
    ".pdf": "documentos",
    ".txt": "documentos",
    ".md": "documentos",
    ".rtf": "documentos",
    ".tex": "documentos",
    ".csv": "documentos",

    # Comprimidos
    ".zip": "comprimidos",
    ".rar": "comprimidos",
    ".7z": "comprimidos",
    ".tar": "comprimidos",
    ".gz": "comprimidos",
    ".bz2": "comprimidos",
    ".xz": "comprimidos",
    ".iso": "comprimidos",

    # Otros
    ".lnk": "accesos_directos",
    ".ini": "configuracion",
    ".log": "logs",
    ".": "otros",
}


# 1. Identifica las carpetas necesarias
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

# 2. Crea solo las carpetas necesarias
for categoria in carpetas_necesarias:
    crear_carpeta(categoria, rutabase)
for categoria, subcarpeta in subcarpetas_necesarias:
    ruta_categoria = os.path.join(rutabase, categoria)
    crear_carpeta(subcarpeta, ruta_categoria)

# 3. Iteramos la lista de todos los archivos
for archivo in todoslosarchivos:
    if archivo == nombre_script:
        continue
    carpeta_origen = os.path.join(rutabase, archivo)
    #Verificamos que no sea una carpeta (esas aun no se como moverlas)
    if os.path.isdir(carpeta_origen) == False:
        nombre, extension = os.path.splitext(archivo) #Separamos el nombre del archivo con su extension
        if extension == "":
            print(f"El archivo '{archivo}' no tiene extensión, se ignorará.")
            archivos_ignorados += 1
            continue
        
        carpeta_destino = os.path.join(rutabase, organizacion.get(extension, "otros"))
        carpeta_destino = os.path.join(carpeta_destino, extension.lstrip("."))

        #Finalmente movemos el archivo a esa carpeta destino
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

print("Finalizado!")
print(f"En total se crearon {carpetas_creadas} carpetas!")
print(f"Total de archivos movidos: {archivos_movidos}")
print(f"Total de archivos que fueron ignorados (por no tener extension, ser carpetas o porque ya existian): {archivos_ignorados}")
print(f"Total de archivos que NO se pudieron mover por permisos: {errores_al_mover}")

print("")
print("........")
input("Presiona Enter para salir...")


# Notas que ayudan a entender el codigo :O
# 1. organizacion[".c"] retorna "codigos" (la carpeta)
# 2. organizacion.get(extension, "otros") retorna tambien la carpeta de la extension, pero si no existe
# entonces retorna "otros"
# 3. La variable "Carpetas_creadas" es global porque se modifica desde una funcion