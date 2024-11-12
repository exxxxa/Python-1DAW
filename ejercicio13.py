num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = str(input("Introduce la operacion que quieres realizar? (Suma,Resta,Multiplicacion,Division): "))

if operacion == "Suma":
    print(num1 + num2)
elif operacion == "Resta":
    print(num1 - num2)
elif operacion == "Multiplicacion":
    print(num1 * num2)
elif operacion == "Division":
    print(num1 / num2)
else:
    print("Operacion no valida")