print("Te voy a pedir la longitud delos tres lados de un triangulo para ver que tipo de triangulo es.")

lado1 = int(input("Introduce el primer lado: "))
lado2 = int(input("Introduce el segundo lado: "))
lado3 = int(input("Introduce el tercer lado: "))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print("Es un triangulo equilatero.")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Es un triangulo escaleno.")
else:
    print("Es un triangulo isosceles.")