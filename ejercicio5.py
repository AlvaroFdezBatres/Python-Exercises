# Escriba un programa que pregunte cuantos nu meros se van a introducir, pida
# esos numeros y escriba cuantos negativos ha introducido.
print("")
cont = int(input("¿Cuántos números van a introducirse? "))
neg = 0
for i in range(0,cont,1):
    x = int(input("Escriba un número: "))
    if(x < 0):
        neg+=1
    i+=1
print(f"Se han introducido {neg} números negativos")