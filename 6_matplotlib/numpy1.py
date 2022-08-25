'''
em redes neurais profundas, laços dentro de laços, com a ideia de Big Data, 
pode aumentar a complexidade/esforço pois, há multiplicações de matrizes/vetores..... 
dessa forma, python fornece o conceito de vetorização via numpy e o método dot()
'''

import numpy as np
import time

#a = np.array([1,2,3,4])
#print(a)

a = np.random.rand(1000000000)
b = np.random.rand(1000000000)

inicio = time.time()
c = np.dot(a,b)
fim = time.time()

#print(c)
print("Soluçao vetorizada: " + str(1000*(fim - inicio)) + " ms")


#solução não vetorizada, ou seja, uso clássico de for
c = 0
inicio = time.time()
for i in range(10000000):
  c += a[i] * b[i]
fim = time.time()

#print(c)
print("Soluçao com for: " + str(1000*(fim - inicio)) + " ms")
  
#ou seja, a solução vetorizada é (aproximado) 300 vezes mais rápida neste exemplo  