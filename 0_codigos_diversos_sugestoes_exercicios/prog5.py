from random import randint, shuffle

def popula_lista(lista, n):
    for i in range(n):
        lista.append(randint(0,50))

def exibe_lista(lista):
    print(lista)

lista = []
popula_lista(lista, 5)
exibe_lista(lista)

outra_lista = [1,2,3,4,5,6,7,8,9]
print(outra_lista)
shuffle(outra_lista)
print(outra_lista)