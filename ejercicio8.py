ciclo = str(input("¿Que ciclo estas cursando? (ASIR, DAM, DAW, SMR): "))
curso = int(input("¿Que año estas cursando? (1 o 2): "))

if ciclo == "ASIR" and curso == 1 or ciclo == "DAW" and curso == 2:
    print("Das despliegue de páginas web")
else:
    print("No das despliegue de páginas web")