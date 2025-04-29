import matplotlib.pyplot as plt
# Datos de ejemplo
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
ventas = [1500, 1800, 1200, 1700, 2100]
# Crear el gráfico de líneas con color
plt.plot(meses, ventas, color='blue', marker='o', linestyle='--')
# Etiquetas en español
plt.xlabel('Meses')
plt.ylabel('Ventas en USD')
plt.title('Ventas Mensuales')
# Mostrar el gráfico
plt.show()
