import pathlib
import os
from humanize import naturalsize
path = r"C:\Users\User\Downloads"
directorio = pathlib.Path(path)
ficheros = [fichero.name for fichero in directorio.iterdir() if fichero.is_file()]
print(ficheros)
sizes = []
for files in ficheros:
    size = os.stat(os.path.join(path, files)).st_size
    sizes.append(naturalsize(size))
print(sizes)
