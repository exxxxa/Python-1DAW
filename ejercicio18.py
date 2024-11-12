precioArticulo = 8.75
cantidadProductos = int(input("¿Cuantos productos quieres comprar?"))

if cantidadProductos >=1 and cantidadProductos<=10:
    calcular = cantidadProductos * precioArticulo
    print(f"No hay descuento, te va a costar {calcular}")
elif cantidadProductos >=11 and cantidadProductos<=50:
    descuento = cantidadProductos * precioArticulo * 0.05
    calcular = cantidadProductos * precioArticulo - descuento
    print(f"Te voy a descontar {descuento}, te va a costar {calcular}")
elif cantidadProductos >=51 and cantidadProductos<=100:
    descuento = cantidadProductos * precioArticulo * 0.1
    calcular = cantidadProductos * precioArticulo - descuento
    print(f"Te voy a descontar {descuento}, te va a costar {calcular}")
else:
    descuento = cantidadProductos * precioArticulo * 0.15
    calcular = cantidadProductos * precioArticulo - descuento
    print(f"Te voy a descontar {descuento}, te va a costar {calcular}")
