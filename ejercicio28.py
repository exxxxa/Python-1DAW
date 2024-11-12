i = 0

while True:
    num = int(input("Inserta un numero: "))

    if i == 0:
        numMin = num
        numMax = num
    if num == 0:
        break

    if num > numMax:
        numMax = num
    if num < numMin:
        numMin = num

    i += 1
    mediaAritmetica = num / i
print(f"El número maximo es {numMax} y el mínimo es {numMin} y la media aritmetica es {mediaAritmetica}")
