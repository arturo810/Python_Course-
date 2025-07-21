# 1. Declara una variable con tu nombre completo y muéstrala.
nombre_completo = "Arturo De Jesus Martinez"
print(nombre_completo)

# 2. Declara una frase y muestra cuántos caracteres tiene.
frase = "Hola reforzando los Fundamentos"
print(len(frase))

# 3. Convierte una cadena a mayúsculas.
cadena = "hola mundo"
print(cadena.upper())

# 4. Convierte una cadena a minúsculas
cadena = "DE JESUS"
print(cadena.lower())

# 5. Extrae la primera letra de una cadena.
cadena = "Python"
print(cadena[0])

# 6. Extrae los últimos cuatro caracteres de una cadena.
cadena = "Programación"
print(cadena[-4:])

# 7. Concatena tu nombre y apellido en una sola cadena.
nombre = "Juan"
apellido = "Pérez"
print(nombre + " " + apellido)

# 8. Usa un f-string para decir: "Hola, me llamo [nombre] y tengo [edad] años".
nombre = "Ana"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} años")

# 9. Repite una palabra tres veces usando *.
palabra = "hola"
print(palabra * 3)

# 10. Une una lista de palabras ['Hola', 'mundo'] en una sola cadena separada por espacios.
palabras = ['Hola', 'mundo', 'ADJM']
print(" ".join(palabras))

# 11. Reemplaza una palabra dentro de una cadena.
frase = "Me gusta Java"
print(frase.replace("Java", "Python"))

# 12. Busca la posición de la palabra "Python" en la frase "Estoy aprendiendo Python en línea".
frase = "Estoy aprendiendo Python en línea"
print(frase.find("Python"))

# 13. Verifica si una cadena contiene la palabra "data".
cadena = "La ciencia de datos es interesante"
print("data" in cadena)

# 14. Divide una cadena usando un separador como una coma o espacio.
cadena = "uno-dos-tres-cuatros"
print(cadena.split("-"))

# 15. Elimina los espacios al inicio y al final de una cadena.
cadena = "   texto con espaciosss   "
print(cadena.strip())

# 16. Invierte el contenido de una cadena.

cadena = "Python"
print(cadena[::-1])

# 18. Cuenta cuántas veces aparece la letra "a" en una cadena.
cadena = "banana"
print(cadena.count("a"))

# 19. Reemplaza todas las vocales de una cadena por "*".
cadena = "Hola mundo"
vocales = "aeiouAEIOU"
resultado = ''.join(['*' if c in vocales else c for c in cadena])
print(resultado)

# 20. Crea una nueva cadena con la primera letra en mayúscula y el resto en minúsculas.
cadena = "pYTHON"
print(cadena.capitalize())

# Usar f
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimando/a {nombre_asociado}, su número de asociado es: {numero_asociado}")
