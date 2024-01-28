# Escriba un programa que pregunte cua ntos nu meros se van a introducir, pida esos
# nu meros, y escriba el mayor, el menor y la media aritmetica. Recuerda que la media
# aritme tica de un conjunto de valores es la suma de esos valores dividida por la cantidad de
# valores.
valores = int(input("¿Cuántos números vas a introducir? "))
menor = float('inf')
suma = 0
max = float('-inf')
for i in range(0,valores):
    n = int(input("Dime un número: "))
    if(n < menor):
        menor = n
    if(n > max):
        max = n
    suma+=n
print(f"EL número mayor es: {max}")
print(f"EL número menor es: {menor}")
print(f"La media es: {suma/valores}")

