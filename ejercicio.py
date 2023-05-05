#set de libros prestados
libros_prestados = {"Cien años de soledad", "El amor en los tiempos del colera", "La ciudad y los perros", "La casa verde", "El tunel"}

#cantidad de libros prestados
print("La cantidad de los libros prestados es: ",len(libros_prestados))

#crear conjunto de libros devueltos
libros_devueltos = {"Cien años de soledad", "La casa verde", "La ciudad y los perros"}

libros_sin_devolver = libros_prestados.difference(libros_devueltos)
print(libros_sin_devolver)