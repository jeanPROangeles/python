import pandas as pd

# lee el archivo excel a traves de la funcion de pandas y lo almacena en el objeto df
df = pd.read_excel('Libro1.xlsx')
#se utilizat to_csv para guardar el archivo en formato csv
df.to_csv('Libro_csv.csv', index=False)