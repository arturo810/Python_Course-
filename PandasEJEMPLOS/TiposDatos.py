"""Utilizando la biblioteca Pandas,
crea un DataFrame llamado df_empleados que contenga dos columnas: nombre y edad.
La columna nombre debe contener los nombres de tres empleados: 'Ana', 'Luis' y 'Carlos'
La columna edad debe contener las edades correspondientes: 30, 25 y 40
Finalmente, muestra el DataFrame df_empleados utilizando la función print().
"""
import pandas as pd
datos = {
   "nombre": ['Ana','Luis','Carlos'],
   'edad':[30,25,40]
}
df = pd.DataFrame(datos)
#print(df)

edades = df["edad"]
print(edades)
print(type(edades))

shape_df = df.shape       # Devuelve (filas, columnas)
columns_df = df.columns   # Devuelve los nombres de columnas
index_df = df.index       # Devuelve el índice (por defecto: RangeIndex)


print("Forma del DataFrame (filas, columnas):", shape_df)
print("Columnas del DataFrame:", columns_df)
print("Índice del DataFrame:", index_df)

























