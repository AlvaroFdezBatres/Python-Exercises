#Introduce un número y di si es primo o no
import math
n = int(input("Introduce un número mayor que 0: "))
cont = 0
if(n > 0):
    for i in range(1,n+1,1):
        if(n%i==0):
            cont+=1
    if(cont > 2):
        print(f"El número {n} no es primo") 
    else:
        print(f"El número {n} es primo")        
else:
    print("Número incorrecto.")
print("")
#print("OTRA FORMA")
print("")
def esPrimo(x):
    if(x > 0):
        if(x < 2):
            print(f"El número {x} es primo")
            return False
        for i in range(2, int(math.sqrt(x))+1): #busco si es divisible entre 2 y el resultado de hacer su raiz cuadrada + 1 y lo pongo positivo con el int
            if(n % i== 0):
                return False
        return True 
    else:
        print("Número incorrecto.")

x = int(input("Introduce un número mayor que 0: "))

if esPrimo(x):
    print(f"El número {x} es primo")
else:
    print(f"El número {x} no es primo")