#Introduce un número y di si es primo o no
n = int(input("Introduce un número: "))
contador = 0

for i in range(1, n + 1):
    if n % i == 0:
        contador += 1

if contador == 2:
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")