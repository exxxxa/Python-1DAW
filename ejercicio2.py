numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

if numero1 > numero2:
    print(f"{numero1} es mayor a {numero2}")
elif numero2 > numero1:
    print(f"{numero2} es mayor a {numero1}")
else:
    print("Son iguales")