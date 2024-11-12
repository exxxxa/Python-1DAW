diaTaxi = str(input("¿Que día de la semana vas a coger el taxi? "))
hora = int(input("¿A que hora vas a coger el taxi? "))
kilometros = float(input("¿Cuantos kilometros vas a hacer? "))

if diaTaxi == "Lunes" or diaTaxi == "Martes" or diaTaxi == "Miercoles" or diaTaxi == "Jueves" or diaTaxi == "Viernes":
    if hora >= 8 and hora <= 18:
        calcular = kilometros * 1 + 3.5
        print(f"Te voy a cobrar {calcular}")
    elif hora >=19 and hora <=23:
        calcular = kilometros * 1.2 + 3.5
        print(f"Te voy a cobrar {calcular}")
    elif hora >=23 or hora <=7:
        calcular = kilometros * 1.5 + 3.5
        print(f"Te voy a cobrar {calcular}")

elif diaTaxi == "Sabado":
    if hora >= 8 and hora <= 18:
        calcular = kilometros * 1.2 + 3.5
        print(f"Te voy a cobrar {calcular}")
    elif hora >= 19 and hora <=8:
        calcular = kilometros * 1.5 + 3.5
        print(f"Te voy a cobrar {calcular}")

elif diaTaxi == "Domingo":
    calcular = kilometros * 1.5 + 3.5
    print(f"Te voy a cobrar {calcular}")
