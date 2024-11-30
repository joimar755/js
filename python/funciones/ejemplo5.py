'''
Parámetros de tipo lista
• Escribir un programa que defina por asignación una lista de 6 enteros en el bloque 
principal del programa. Elaborar tres funciones, la primera recibe la lista y retorna la 
suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la 
última recibe la lista y retorna el menor.
suma=suma+lista[x]
• Escribir una función que reciba una lista de string y nos retorne el que tiene más 
caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que 
tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))
'''
def suma_list (list):
    return sum(list) 
def max_list (list):
    return max(list) 
def min_list (list):
    return min(list) 

numeros = [10,20,30,40,50,60]

print('suma lista: ', suma_list(numeros))
print('suma lista: ', max_list(numeros))
print('suma lista: ', min_list(numeros))
