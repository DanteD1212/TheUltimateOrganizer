# 📂 Organizador de Archivos Automático

¡Mantén tu espacio de trabajo digital limpio y organizado sin esfuerzo! Este script de Python clasifica y mueve automáticamente tus archivos en carpetas designadas, eliminando el desorden de tus directorios.

---

## ✨ Características Principales

- **Clasificación Automática:** Organiza archivos por tipo (imágenes, documentos, códigos, etc.) en carpetas específicas.
- **Creación Inteligente de Carpetas:** Crea automáticamente las carpetas principales y subcarpetas necesarias si no existen.
- **Selección de Directorio:** Permite especificar qué carpeta deseas organizar, funcionando en cualquier ubicación de tu sistema.
- **Manejo Robusto de Errores:** Gestiona permisos insuficientes y evita sobrescribir archivos existentes.
- **Informes Detallados:** Al finalizar, muestra un resumen con el número de carpetas creadas, archivos movidos, ignorados y errores de permisos.
- **Manejo de Casos Especiales:** Archivos sin extensión se ignoran y extensiones desconocidas se mueven a la carpeta "otros".

---

## 🚀 Cómo Usar

1. **Descarga el Ejecutable:**

   - Ve a la sección [Releases](releases/) y descarga el archivo `THE_Organizer.exe`.

2. **Ejecuta el Programa:**

   - Haz doble clic en `THE_Organizer.exe`. Se abrirá una ventana de consola.
   - _Nota:_ Si tu antivirus bloquea la ejecución, puedes revisar el código fuente en [`organizer.py`](organizer.py) para verificar su seguridad.

3. **Introduce la Ruta:**

   - El programa te pedirá la ruta completa de la carpeta que deseas organizar.
   - Si la ruta es incorrecta, podrás reintentar. Para salir, escribe `s` y presiona Enter.

   **Ejemplos de ruta:**

   - Windows: `C:\Users\TuUsuario\Downloads`
   - macOS/Linux: `/home/TuUsuario/Documents/UnsortedFiles`

4. **Observa la Magia:**
   - Tras ingresar una ruta válida, el script organizará los archivos y mostrará un resumen de las acciones realizadas.

---

## 🗂️ Categorías de Organización

El organizador clasifica los archivos en las siguientes categorías principales (y subcarpetas por extensión):

- **imagenes** (ej: `.png`, `.jpg`, `.drawio`, `.webp`)
- **codigos** (ej: `.py`, `.java`, `.html`, `.css`)
- **instaladores** (ej: `.exe`, `.msi`, `.apk`)
- **audios** (ej: `.mp3`, `.wav`, `.flac`)
- **videos** (ej: `.mp4`, `.mkv`, `.avi`)
- **documentos** (ej: `.pdf`, `.docx`, `.txt`, `.csv`)
- **comprimidos** (ej: `.zip`, `.rar`, `.7z`)
- **otros** (ej: `.lnk`, `.ini`, `.log` y cualquier extensión no definida o archivos sin extensión)

Puedes revisar el archivo [`organizer.py`](organizer.py) para ver la lista completa de extensiones soportadas y sus categorías. ¡Siéntete libre de modificar el diccionario `organizacion` para añadir o cambiar categorías!

---

## ⚠️ Manejo de Casos Especiales

- **Archivos sin extensión:** Serán ignorados y contados en el total de "archivos ignorados".
- **Extensiones no reconocidas:** Se moverán a la carpeta "otros".
- **Archivos ya existentes en destino:** No se moverán para evitar sobrescribir datos y se contará como "ignorados".
- **Errores de permiso:** Si no tienes permisos para mover un archivo, se informará y contará en "errores al mover".
- **Carpetas:** Las carpetas existentes en el directorio a organizar serán ignoradas y no se moverán.

---

## 👨‍💻 Autor

[DanteD1212](https://github.com/DanteD1212)
