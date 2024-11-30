'''
: Funciones con Parámetros por Defecto
 - Escribe una función llamada `descuento` que tome el precio de un producto y un 
porcentaje de descuento. La función debe retornar el precio final después de aplicar el 
descuento. Si no se proporciona el porcentaje de descuento, debe asumir que es 10%.
precio=int(input("Ingrese el precio: "))
''' 
def descuentno(precio, porcentaje=10):
    return precio - (precio * (porcentaje /100)) 

precio = int(input('ingreso el precio: ')) 
print('precio con descuento es: ',descuentno(precio))
print('precio con descuento es: ',descuentno(precio, 20))