import os
from humanize import naturalsize
#recursivo
ficheros_recursivo = []
path_carpeta_personal = r"C:\Users\User"
for nombre_dir, dirs, ficheros in os.walk(path_carpeta_personal):
    print(ficheros, end = " ")
    print(naturalsize(os.stat(nombre_dir).st_size))

        