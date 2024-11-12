ciclo = str(input("¿En que ciclo estas? (SMR, ASIR, DAW, DAM): "))
curso = int(input("¿Que año estas cursando? (1 o 2): "))

if ciclo == "DAW" and curso == 1 or ciclo == "DAM" and curso == 1:
    print("Das programación")
else:
    print("No das programación")