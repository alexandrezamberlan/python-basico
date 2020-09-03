from random import randint

def popular_lista(lista, n):
    for i in range(n):
        lista.append(randint(0,40))
    
def exibir_lista(lista):
    for i in lista:
        print(i)

def maior_valor_par(lista):
    maior_par = -1
    
    for i in range(len(lista)):
        if (lista[i] % 2 == 0 and lista[i] > maior_par):
            maior_par = lista[i]
        
    return maior_par

lista = []
popular_lista(lista,10)
exibir_lista(lista)

print("O maior valor par é ", maior_valor_par(lista))