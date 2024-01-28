# Escriba un programa que pregunte cuantos nu meros se van a introducir, pida
# esos numeros, y muestre un mensaje cada vez que un nu mero no sea mayor que el
# anterior.
print("")
cont = int(input("¿Cuántos números van a introducirse? "))
iter = 0
aux = None #No tiene valor

while iter < cont:
    n = int(input("Introduce un número: "))
    if aux is not None and n <= aux: #compruebo si la variable 'aux' tiene valor 
        print(f"El número {n} no es mayor que el anterior: {aux}")
    aux = n
    iter += 1
