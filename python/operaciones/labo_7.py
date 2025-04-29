import numpy as np 

def vector_fun():
 vector = np.arange(1, 11)
 print('el vector es:', vector)
 print('suma:',np.sum(vector))
 print('media:',np.mean(vector))
 print('max:',np.max(vector))
 print('min:',np.min(vector))


def matriz_zeros():
 vector = np.zeros((3, 4))
 print('la matriz de ceros es:', vector) 
 vector_cambio = vector.reshape(2,6)
 print('la matriz de ceros cambiada de forma es:', vector_cambio) 
 
def trans():
 matriz = np.random.rand(3,3) 
 print('matriz original:\n', matriz)
 print('la matriz transpuesta es:\n', matriz.T)

def dos_array():
    array1 = np.array([1,2,3,4,5,])
    array2 = np.array([6,7,8,9,10])
    array_concatenado = np.concatenate((array1, array2))
    print('el array concatenado es:', array_concatenado)
#matriz_zeros()
#trans()
dos_array()