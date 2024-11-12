suma = 0
haInsertadoCero = False

while not haInsertadoCero:
    num = int(input("Inserta un número: "))
    if num == 0:
        haInsertadoCero = True
    suma += num

print(f"La suma de los números introducidos es: {suma}")