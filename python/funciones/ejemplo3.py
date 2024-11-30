'''
Uso de Funciones con Parámetros Arbitrarios
 - Escribe una función llamada `mayor_valor` que acepte un número arbitrario de argumentos 
y retorne el mayor valor
'''
def mayor_val(*args):
    return max(args)
print('el mayor valor', mayor_val(10,100,50,900,500))