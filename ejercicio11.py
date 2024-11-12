edadUsuario = int(input("Ingrese su edad: "))

if edadUsuario >=0 and edadUsuario<=2:
    print("Eres un bebe")
elif edadUsuario >=3 and edadUsuario<=12:
    print("Eres un niño")
elif edadUsuario >=13 and edadUsuario<=17:
    print("Eres un Adolescente")
elif edadUsuario >=18 and edadUsuario<=34:
    print("Eres adulto pero no")
elif edadUsuario == 35:
    print("La mejor edad posible")
elif edadUsuario >=35 and edadUsuario<=50:
    print("Audlto")
elif edadUsuario >=51 and edadUsuario<=67:
    print("Pre-anciano")
elif edadUsuario >=68 and edadUsuario<=99:
    print("Anciano")
else:
    print("Centenario")