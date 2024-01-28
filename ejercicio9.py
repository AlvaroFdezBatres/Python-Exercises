# Escriba un programa que pida do nu meros enteros y escriba la suma de todos los
# enteros desde el primer numero hasta el segundo.
#Mejora el programa anterior haciendo que el programa escriba la suma realizada
n1 = int(input("Dame un número: "))
n2 = int(input("Dame otro número: "))

if(n1 > n2):
    aux = n1
    n1 = n2
    n2 = aux
suma = 0
cadena = ""
for i in range(n1,n2,1):
    # cadena = cadena + str(i) +"+"
    #el "end=" " se utiliza para buscar el caracter que le indique y cuando lo encuentra acaba
    print(f"{i} + ",end=" ")
    suma = suma + i
suma+=n2   
print(f"{n2} = {suma}")