def orden_numeros(n1,n2,n3):
  if n1 > n2 and n1 > n3:
        if n2 > n3: 
            return (n1, n2, n3)
        else:
            return (n1, n3, n2)
  elif n2 > n1 and n2 > n3:
        if n1 > n3:
            return (n2, n1, n3)
        else:
            return (n2, n3, n1)
  else:
        if n1 > n2:
            return (n3, n1, n2)
        else:
            return (n3, n2, n1)

n1 = int(input("Ingrese un número "))
n2 = int(input("Ingrese un número "))
n3 = int(input("Ingrese un número "))
print(orden_numeros(n1,n2,n3))
    
    

   
        
 

