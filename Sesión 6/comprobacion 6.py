def analisis_numero(n):
    if n >= 0:
     if n == 0:
       return("El número es 0")
     else:
      return("El número es positivo")
  
    else:
     return("El número es negativo")

n = int(input("Ingrese un número "))
print(analisis_numero(n))
