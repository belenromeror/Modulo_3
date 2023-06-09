
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

# Crear un diccionario vacío
result_dict = {}

# Recorrer cada sublista y cada elemento dentro de ellas
for i in range(len(lista)):
    # Si el primer número es cero, omitir la sublista
    if lista[i][0] == 0:
        result_dict[chr(i+65)] = lista[i]
        continue
    # Si hay un cero en cualquier otra posición, omitir solo la impresión del cero
    for j in range(len(lista[i])):
        if lista[i][j] == 0:
            continue
        # Imprimir cada número no cero en la sublista
        print(lista[i][j])
        # Asignar cada sublista al diccionario correspondiente, se debe agregar para considerar todas las listas.
        result_dict[chr(i+65)] = lista[i]

# Imprimir el diccionario resultante
print(result_dict)