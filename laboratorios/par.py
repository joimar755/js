''' Crear un script que pida al usuario un número y determine si es par o impar 
utilizando condicionales (if, else).
 '''
numero = int(input('ingrese un numero: '))

if numero % 2 == 0 :
    print(f'{numero} es par')
else:
    print(f'{numero} es impar')