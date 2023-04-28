def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    else:
        return a / b

def operaciones(a, b):
    result_dict = {
        "Suma": suma(a, b),
        "Resta": resta(a, b),
        "Multiplicación": multiplicacion(a, b),
        "División": division(a, b)
    }
    return result_dict

a = float(input("Ingrese un número: "))
b = float(input("Ingrese otro número: "))

resultados = operaciones(a, b)

print(resultados)