#Escriba un programa que pida dos nu meros enteros y escriba que nu meros son pares y
# cuales impares desde el primero hasta el segundo. 
print("")
print("PARES E IMPARES")
n1 = int(input("Escriba un número entero: "))
n2 = int(input(f"Escriba un número entero mayor o igual que {n1}: "))
while n1 > n2:
    print(f"¡Le he pedido que escriba un número mayor o igual que {n1}!")
    print("PARES E IMPARES")
    n1 = int(input("Escriba un número entero: "))
    n2 = int(input(f"Escriba un número entero mayor o igual que {n1}: "))
for i in range(n1,n2,1):
    if(i%2 == 0):
        print(f"El número {i} es par.")
    else:
        print(f"El número {i} es impar.")
print("")