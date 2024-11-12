notasUsuario = int(input("Introduce tu calificación númerica (0 a 100): "))

if notasUsuario >=90 and notasUsuario <=100:
    print("A")
elif notasUsuario >=80 and notasUsuario <=89:
    print("B")
elif notasUsuario >=70 and notasUsuario <=79:
    print("C")
elif notasUsuario >=60 and notasUsuario <=69:
    print("D")
elif notasUsuario <=59:
    print("F")
else:
    print("No has insertado una nota válida")
    