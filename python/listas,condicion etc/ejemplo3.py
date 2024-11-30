'''
Parte 2: Bucles con Listas
- Bucle while: En una empresa trabajan n empleados cuyos sueldos oscilan entre $1.000.000 y
$5.000.000, realizar un programa que lea los sueldos que cobra cada empleado e informe
cuántos empleados cobran entre $1.000.000 y $3.000.000 y cuántos cobran más de $3.000.000.
Además el programa deberá informar el total que gasta la empresa en sueldos al personal.
n=int(input("Cuantos empleados tiene la empresa:"))
x=1
conta1=0
conta2=0
gastos=0
while x<=n:
 sueldo=float(input("Ingrese el sueldo del empleado:"))
 # continuar con el condicional
'''
n=int(input("Cuantos empleados tiene la empresa:"))
x=1
conta1=0
conta2=0
gastos=0
while x<=n:
 sueldo=float(input("Ingrese el sueldo del empleado:"))
 gastos += sueldo
 if sueldo >= 1000000 and sueldo <= 3000000: 
     conta1+=1
 elif  sueldo > 3000000: 
     conta2+=1 
 x += 1

print(f'cantidad empleados 1 y 3 M :{conta1}')
print(f'cantidad empleados mas de 3 M :{conta2}')
print(f'gastos :{gastos}')
