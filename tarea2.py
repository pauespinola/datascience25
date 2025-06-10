
precio_producto= int("24000")
print(f"Compre aquí su mat de yoga. Precio unitario: $ {precio_producto} pesos.")
cantidad= int(input("Ingrese la cantidad de artículos que comprará: "))
descuento= int("10")
totalsindescuento= precio_producto*cantidad
monto_descuento= int((descuento/100)*totalsindescuento)
total_con_descuento= totalsindescuento-monto_descuento
print(f"El subtotal de su compra es ${totalsindescuento}")
print(f"Monto de descuento: ${monto_descuento}")
print(f"El total de su compra es: ${total_con_descuento} pesos.")