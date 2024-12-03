''' Crear un juego de adivinanza donde el programa genere un número aleatorio y el 
usuario deba adivinarlo, recibiendo pistas de "mayor" o "menor" en cada intento '''
import random
numeroAleatorio = random.randrange(1, 9) 

numeroUsuario = 0
pista = "" 
intento = 0

while numeroUsuario != numeroAleatorio:
    numeroUsuario = int(input("Adivina un número (entre 1 y 8): "))
    intento += 1
    if numeroUsuario > numeroAleatorio:
        pista = print("menor", numeroAleatorio)
    elif numeroUsuario < numeroAleatorio:
        pista = print("mayor", numeroAleatorio)
        
print("el numero de intentos fueron", intento)
        