Temperatura = str(input("¿Que temperatura vas a darme? (Celsius, Fahrenheit): "))
numeroTemperatura = float(input("Introduce la temperatura: "))

if Temperatura == "Celsius":
    cuenta = numeroTemperatura * 1.8 + 32
    print(f"{cuenta}")
elif Temperatura == "Fahrenheit":
    cuenta = numeroTemperatura * 1.8 + 273.15
    print(f"{cuenta}")