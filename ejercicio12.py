# 11. Escriba un programa que pida un nu mero entero mayor que cero y calcule su factorial.
print("FACTORIAL")
n = int(input("Dime un número entero mayor que 0: "))
while(n<=0):
    print("El número que has introducido no es mayor que 0")
    n = int(input("Dime un número entero mayor que 0 "))
factorial = 1
for i in range(1,n+1):
    factorial*=i
print(f"El factorial de {n} es {factorial}")
