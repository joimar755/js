'''
 Crear un diccionario que almacene los nombres de tres estudiantes y sus respectivas 
calificaciones. Escribir un programa que imprima el nombre del estudiante con la calificación 
más alta.
nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación 
de {calificaciones[nombre_max]}.")
'''
estudiantes = {
    'Estudiante 1': 95,
    'Estudiante 2': 80,
    'Estudiante 3': 75
}
print (max(estudiantes,key=estudiantes.get))
print (max(estudiantes.values()))

