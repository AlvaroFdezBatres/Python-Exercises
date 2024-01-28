#Escriba un programa que pregunte cuantos numeros se van a introducir, pida
# esos numeros, y muestre un mensaje cada vez que un numero no sea mayor que el
# primero.
cont = int(input("¿Cúantos números van a introducirse? "))
iter = 1
n = int(input("Introduce un número: "))
while iter < cont:
    x = int(input("Introduce un número: "))
    iter+=1
    if(x<=n):
        print(f"El número {x} no es mayor que {n}")
    
