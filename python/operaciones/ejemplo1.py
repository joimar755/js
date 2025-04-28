import random
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
n1 = random.uniform(1, 5)
n2 = random.uniform(1, 5)
n3 = random.uniform(1, 5)
#x = input("Ingrese una frase: ")
#y = bool(input("Ingrese un valor booleano (True/False): "))

    
suma = a + b
resta = a - b 
multiplicacion = a * b
division = a / b if b != 0 else "No se puede dividir por cero"


print("El número ingresado es:", a)
print("El número ingresado es:", b)
#print("La frase ingresada es:", x)
#print("El valor booleano ingresado es:", y)
operaciones = {
    "Suma": suma,
    "Resta": resta,
    "Multiplicación": multiplicacion,
    "División": division
}
notas = {
    "Nota 1": n1,
    "Nota 2": n2,
    "Nota 3": n3,
    "Promedio": (n1 + n2 + n3) / 3,
    "aprobo": (n1 + n2 + n3) / 3 >= 3.0,
    "Desaprobó": (n1 + n2 + n3) / 3 < 3.0 
}

print("Resultados de las operaciones:", operaciones) 
print("--------------Resultados de las operaciones:------------------")
for reultado in operaciones:
    print(f"{reultado}: {operaciones[reultado]}")
    
print("--------------Notas:------------------")
for nota in notas:
    print(f"{nota}: {round(notas[nota],2)}")