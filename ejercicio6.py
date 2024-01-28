# Escriba un programa que pregunte cuantos nu meros se van a introducir, pida
# esos numeros, y diga al final cuantos han sido pares y cuantos impares.
print("")
cont = int(input("¿Cuántos números van a introducirse? "))
par = 0
impar = 0
for i in range(0,cont,1):
    x = int(input("Escriba un número: "))
    if(x%2 == 0):
        par+=1
    else:
        impar+=1
    i+=1
print(f"Se han introducido {par} números pares y {impar} números impares.")