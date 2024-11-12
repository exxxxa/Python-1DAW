pesoCoche = float(input("Introduce el peso del coche (en toneladas): "))

if pesoCoche<=1:
    print("Es ligero")
elif pesoCoche >= 1 and pesoCoche<=2:
    print("Es peso medio")
else:
    print("Es pesado")