''' Crear un diccionario simple que almacene información de contacto (nombre, 
correo) y mostrar sus claves y valores '''

contactos = {
    'nombre': 'juan',
    'correo':'juan@gmail.com'
    }

for clave , valor in contactos.items():
    print(clave,":",valor)
