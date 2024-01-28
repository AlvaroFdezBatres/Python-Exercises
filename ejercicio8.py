# Escriba un programa que pregunte cuantos nu meros se van a introducir, pida esos
# nu meros (que puedan ser decimales) y calcule su suma.
numeros = int(input("¿Cúantos números van a introducir?"))
suma = 0
for i in range(0,numeros):
    n = float(input("Dame un número: "))
    suma+=n
print(f"La suma total es: {suma}")