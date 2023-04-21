#Calculo de factorial de un número
#Factorial es todos los números entre el número y uno

def factorial_iterativo(n):
    result = 1
    contador = n
    while contador > 0:
        result *= contador  # result = result * contador
        contador -= 1
    return result 

a = input("Ingrese un número ")
print(factorial_iterativo(int(a)))

