#Definir constante
MAGOS = {"Harry Houdini", "David Blaine", "Teller"}
CIENTIFICOS = {"Newton","Hawking","Einstein"}

#definir categorias
magos = []
científicos = []
otros = []

#lista de nombres
nombres = ["Harry Houdini","Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

for nombre in nombres:
    if nombre in MAGOS:
        magos.append(nombre)
    elif nombre in CIENTIFICOS:
        científicos.append(nombre)
    else:
        otros.append(nombre)


def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = ("El gran " + magos[i])


def imprimir_nombres(lista):
    for elementos in lista:
        print(elementos)
        

#Imprimir todos los nombres
print("Todos los nombres")
imprimir_nombres(nombres)

#Imprimir los nombres de los magos
hacer_grandioso(magos)
print("Nombre de los magos grandiosos")
imprimir_nombres(magos)

#Imprimir los nombres de los cientificos
print("Nombre de los cientificos")
imprimir_nombres(científicos)

#Imprimir los nombres de los otros
print("Nombres restantes")
imprimir_nombres(otros)