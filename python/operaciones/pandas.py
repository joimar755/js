import pandas as pd 

data = {'Nombre': ['Juan', 'Ana', 'Pedro', 'María', 'Luis'],
        'profesion': ['Ingeniero', 'Médico', 'Abogado', 'Arquitecto', 'Diseñador'],
        'pais': ['España', 'México', 'Colombia','ecuador','francia'],}

df = pd.DataFrame(data)
print(df)