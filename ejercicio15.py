figuraUsuario = str(input("¿El area de que figura geometrica quieres calcular? (Triangulo,Rectangulo o Circunferencia):  "))

if figuraUsuario == "Triangulo":
    base = int(input("Introduce la base: "))
    altura = int(input("Introduce la altura: "))
    area = base * altura
    print(area)
elif figuraUsuario == "Rectangulo":
    largo = int(input("Introduce el largo: "))
    ancho = int(input("Introduce el ancho: "))
    area = largo * ancho
    print(area)
elif figuraUsuario == "Circunferencia":
    radio = int(input("Introduce el radio: "))
    area = 3.14*(radio*radio)
    print(area)