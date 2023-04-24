#Lista entregada
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for sublista in lista:
    if sublista[0] == 0:
        continue
    
    for elemento in sublista:
        if elemento == 0:
            continue
        
        print(elemento)