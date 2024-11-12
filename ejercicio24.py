nombreUsuario = str(input('Nombre del usuario: '))
contrasenaUsuario = input("Inserta la contraseña: ")
contrasenaConfirmacion = input("Inserta la contraseña de nuevo: ")


while contrasenaUsuario != contrasenaConfirmacion:
    contrasenaConfirmacion = input("Inserta la contraseña: ")
    contrasenaUsuario = input("Inserta la contraseña de nuevo: ")
    if contrasenaUsuario == contrasenaConfirmacion:
        break
print("Cuenta creada con exito")