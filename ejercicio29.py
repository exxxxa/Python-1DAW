"""Haz un programa que simule el registro de un usuario. Deberá pedirle su nombre y contraseña.
 Para asegurarnos que no escribe mal la contraseña se le pedirá que la ingrese dos veces.
Mientras que las dos contraseñas no coincidan se le debe pedir que ingrese la contraseña."""


nombreUsuario = input("Introduce tu nombre de usuario: ")
contraCorrecta = False

while not contraCorrecta:
    contra1 = input("Introduce tu contraseña: ")
    contra2 = input("Introduce de nuevo tu contraseña: ")
    if contra1 == contra2:
        contraCorrecta = True
    else:
        print("Las contraseñas no coinciden")

print("Usuario creado correctamente")