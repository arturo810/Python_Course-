# Importamos la biblioteca pandas y la renombramos como 'pd'
import pandas as pd

# Creamos un diccionario con los datos que usaremos
# Cada clave representa una columna, y cada valor es una lista de los datos en esa columna
datos = {
    "nombre": ["Juan", "Ana", "Luis"],  # Columna de nombres
    "edad": [25, 30, 22]                # Columna de edades
}

# Convertimos el diccionario a un DataFrame, que es una estructura de tabla
df = pd.DataFrame(datos)

# Mostramos el DataFrame completo por consola
print(df)

# Podemos acceder a una sola columna usando el nombre entre corchetes
print(df["nombre"])  # Imprime solo la columna de nombres

# También podemos acceder a una fila por su índice (por ejemplo, la fila 0)
print(df.loc[0])  # Imprime la fila completa con nombre y edad de la primera persona

# Filtrar datos: personas mayores de 23 años
print(df[df["edad"] > 23])











