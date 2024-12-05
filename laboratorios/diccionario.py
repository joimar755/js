''' Crear un diccionario simple que almacene información de contacto (nombre, 
correo) y mostrar sus claves y valores '''

contactos = {
    'nombre': 'juan',
    'correo':'juan@gmail.com'
    }
#update
contactos['nombre'] = 'jose'

#recorrer con un for el diccionario
for clave , valor in contactos.items():
    print(clave,":",valor)
