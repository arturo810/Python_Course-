frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)  # agrega  ["manzana", "banana", "naranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

frutas.sort()  # ordena la lista alfabéticamente.
print(frutas)  # Imprime ["manzana", "pera", "uva"]

frutas.reverse() #invierte el orden actual de la lista.
print(frutas)  # Imprime ["uva", "pera", "manzana"]

fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

