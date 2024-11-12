numeroCorrecto = False

while not numeroCorrecto:
    num = int(input("Introduzca un número: "))
    if num >= 0:
        numeroCorrecto = True
    else:
        print("El numero debe ser positivo")

while num != 0:
    print(num)
    num = num-1
print("Ring Ring")