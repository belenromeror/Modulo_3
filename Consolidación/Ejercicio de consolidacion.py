#definir categorias
magos = []
científicos = []
otros = []

#lista de nombres
nombres = ["Harry Houdini","Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

for nombre in nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton","Hawking","Einstein"]:
        científicos.append(nombre)
    else:
        otros.append(nombre)

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = magos[i].replace(magos[i], "El gran " + magos[i])



#Imprimir todos los nombres
print(nombres)

#Imprimir magos
print("Nombre de los magos grandiosos"+str(magos))


 
