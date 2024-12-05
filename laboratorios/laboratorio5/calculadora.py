numero1 = int(input("ingrese numero 1: "))   
numero2 = int(input("ingrese numero 2: "))

suma = numero1 + numero2
multi = numero1 * numero2
resta = numero1 - numero2

print("*****CALCULADORA******")
print(f"la suma es {suma}")
print(f"la multiplicacion  es {multi}")
print(f"la resta  es {resta}")

if numero2 == 0:
    print("no se puede dividir por 0")
else:
    division = numero1 / numero2
    residuo = numero1 % numero2  
    print(f"la division es {division}")
    print(f"el residuo es {residuo}")