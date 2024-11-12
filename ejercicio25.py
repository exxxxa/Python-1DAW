import random

numSecreto = random.randint(0,100)
intentos = 1
haAcertado = False

print("Adivina el número del 0 al 100")

while not haAcertado:
    numUsuario = int(input("Inserta el número: "))

    if numUsuario == numSecreto:
        print(f"Has acertado! con {intentos} intentos")
        haAcertado = True
    elif numUsuario < numSecreto:
        print("Ese no es! Es mayor")
    else:
        print("Ese no es! Es menor")

    intentos += 1