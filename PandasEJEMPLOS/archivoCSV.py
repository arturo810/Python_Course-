import pandas as pd

df = pd.read_csv("C:\CursoPYTHON\PRACTICAS\python\csv\Precipitaciones.csv")

#print(df)
print(df.head()) # ENCABEZADO
print(df.tail()) #  COLA FINAL
print(df.shape)  # MUESTRA LAS FILAS Y LAS COLUMNAS
print(df.columns) # MUESTRA LOS NOMBRES DE LAS COLUMNAS
print(df.info())    #DA INFORMACIÓN
print(df.describe()) 
















