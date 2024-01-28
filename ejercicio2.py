# Escriba un programa que pida un numero entero mayor que cero y que escriba
# sus divisores.
print("")
n = int(input("Escriba un número entero mayor que 0: "))
while n <= 0:
    print(f"¡Le he pedido que escriba un número mayor o igual que 0!")
    n = int(input("Escriba un número entero mayor que 0: "))
cont = 0
for i in range(1,n+1,1):
    if(n%i == 0):
        # print(f"{i} es divisor de {n}")
        print(i, end=" ")
        cont = cont + 1
print(f"Los divisores de {n} son: {cont}", end="")