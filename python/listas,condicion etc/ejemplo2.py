numero = int(input('ingrese un numero: '))


if numero > 0 and numero <=999:
    if numero < 10: 
        print(f'el numero {numero} tiene un digito')
    elif numero < 100: 
        print(f'el numero {numero} tiene dos digitos')
    else:
        print(f'el numero {numero} tiene tres digitos') 
else:
    print(f'el {numero} ingresado no es valido')
        