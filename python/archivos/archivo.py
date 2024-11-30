

with open('mensaje.txt','r') as archivo:
    mensaje = archivo.read() 
    

print(mensaje)
archivo.close()