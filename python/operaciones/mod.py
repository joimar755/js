import random
contador = 0
for n in range(0,5,1):
 n = random.randint(1, 10)
 contador += 1
 print(f'El numero {contador}')
 if n % 2 == 0 :
    print(f' {n} es par')
 else:
    print(f'{n} es impar')