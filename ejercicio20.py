lado1 = int(input("Introduce el primer lado: "))
lado2 = int(input("Introduce el segundo lado: "))
lado3 = int(input("Introduce el tercer lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Los lados dados forman un triangulo válido")
else:
    print("Los lados dados no forman un triangulo")