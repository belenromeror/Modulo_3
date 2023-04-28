#Lista entregada
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
diccionario = {}
for i, sublista in enumerate(lista):
    if sublista[0] == 0:
        continue
    subdiccionario = {}
    for j, elemento in enumerate (sublista):
        if elemento == 0:
            continue
        subdiccionario [f"{chr(ord('A')+i)}{j+1}"] = elemento
    diccionario[chr(ord('A')+i)] = subdiccionario

for  subdiccionario in diccionario.items():
    print(subdiccionario)