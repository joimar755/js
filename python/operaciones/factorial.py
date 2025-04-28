import random
n = random.randint(1, 10)
print(f'El numero es {n}')
if n < 0:
    print("El numero es negativo")
elif n == 0:
    factorial = 1
    print("El numero es cero, su factorial es 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(f"El numero es positivo, su factorial es {factorial}")
