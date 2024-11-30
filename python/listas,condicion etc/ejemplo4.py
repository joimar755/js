'''
Bucle For: Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto
cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
cant1=0
cant2=0
cant3=0
cant4=0
n=int(input("Cantidad de puntos:"))
for f in range(n):
 x=int(input("Ingrese coordenada x:"))
 y=int(input("Ingrese coordenada y:"))
# continuar con el condicional
'''
cant1=0
cant2=0
cant3=0
cant4=0
n=int(input("Cantidad de puntos:"))
for f in range(n):
 x=int(input("Ingrese coordenada x:"))
 y=int(input("Ingrese coordenada y:"))
 if x > 0 and y > 0:
    cant1+=1 
 elif x < 0 and y > 0:
    cant2+=1
 elif x < 0 and y < 0:    
    cant3+=1 
 elif x > 0 and y < 0:
    cant4+=1 
 
print('cantidad cuadrante 1:', cant1)
print('cantidad cuadrante 2:', cant2)
print('cantidad cuadrante 3:', cant3)
print('cantidad cuadrante 4:', cant4)

