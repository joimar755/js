def Saludar():
    print('hola') 
Saludar()
    
def SMS(sms):
    print(sms)

SMS('hola como estas')

def Datos(nombre,edad):
    mens = nombre," ", edad 
    return mens
nombre = input()
edad = int(input()) 
dat = Datos(nombre,edad)
print(dat)