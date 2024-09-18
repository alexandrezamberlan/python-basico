import numpy as np

lista1 = np.array([1, 2, 3, 4, 5, 6])
lista2 = np.array([1, 2, 3, 4, 5, 6])
lista_ok = False
while (not lista_ok):
    lista_ok = True
    np.random.shuffle(lista2)
    for i in range(0,len(lista1)):
        if (lista1[i] == lista2[i]):
            lista_ok = False
            break;
print("Original array: ", lista1)
print("Shuffled array: ", lista2)

