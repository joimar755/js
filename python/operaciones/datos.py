import pandas as pd 
import numpy as np
data = {'Nombre': ['Juan', 'Ana', 'Pedro', 'María', 'Luis'],
        'profesion': ['Ingeniero', 'Médico', 'Abogado', 'Arquitecto', 'Diseñador'],
        'pais': ['España', 'México', 'Colombia','ecuador','francia'],}

df = pd.DataFrame(data)
#print(df)

df = pd.read_csv('data.csv')
#print(df)
np.random.seed(42)
df1 = pd.DataFrame(
  np.random.randint(1, 100, size=(100,8)),
  columns = [f'columna_{i+1}'for i in range(8)] 
)                   

print('las primeras  filas del dataframe son:')
print(df1.head())
print('resumen estadistico del dataframe son:')
print(df1.describe())