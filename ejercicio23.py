num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = str(input("Introduce la operacion que quieres realizar? (Suma,Resta,Multiplicacion,Division): "))

match operacion:
    case "Suma":
        print(num1 + num2)
    case "Resta":
        print(num1 - num2)
    case "Multiplicacion":
        print(num1 * num2)
    case "Division":
        print(num1 / num2)
    case _:
        print("Operacion no valida")