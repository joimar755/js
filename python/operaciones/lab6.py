import pandas as pd

df = pd.read_csv('data_2.csv')
print('las primeros registos dataframe son:')
print(df.head())
print('muestra de los datos:')
print(df.info())
print('describe los datos:')
print(df.describe())

df['precio_total']= df['Precio_unitario'] * df['Cantidad_vendida']
print(df)
df_filtrado = df['Cantidad_vendida'] > 40
print('los datos filtrados son:')
print(df[df_filtrado])
print('los 10 precios mas altos son:')
df_ordanado = df.sort_values(by='Precio_unitario', ascending=False)
print(df_ordanado.head(10))