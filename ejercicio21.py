tipoVia = str(input("Introduce el tipo de via por el que vas a circular (Autovia o Nacional): "))
tipoVehiculo = str(input("Introduce el tipo de vehiculo (Coche,Autobus o Camion): "))

if tipoVia == "Autovia":
    if tipoVehiculo == "Coche":
        print("Tienes que ir a 120km/h")
    elif tipoVehiculo == "Autobus":
        print("Tienes que ir a 110km/h")
    elif tipoVehiculo == "Camion":
        print("Tienes que ir a 100km/h")
    else:
        print("No es un vehiculo válido")

if tipoVia == "Nacional":
    if tipoVehiculo == "Coche":
        print("Tienes que ir a 110km/h")
    elif tipoVehiculo == "Autobus":
        print("Tienes que ir a 100km/h")
    elif tipoVehiculo == "Camion":
        print("Tienes que ir a 90km/h")
    else:
        print("No es un vehiculo valido")
        