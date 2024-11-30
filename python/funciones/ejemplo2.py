'''
 Declaración Básica de Funciones
 - Escribe una función llamada `bienvenida` que tome un nombre como parámetro y salude a 
la persona por su nombre.
 - Escribe una función llamada `area_circulo` que tome el radio de un círculo como parámetro 
y retorne su área. Usa la fórmula: área = π \* radio^2 (puedes usar `math.pi`).
return math.pi * radio ** 2 # realizo la formula
'''
import math
def bienvenida(sms):
    return sms

print(bienvenida('juan'))

def AreaYcircu(radio):
    return math.pi * radio ** 2

print('area del circulo ', AreaYcircu(10))