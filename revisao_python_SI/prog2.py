from random import randint, shuffle

# for i in range(4,10):
#     print(i)
    
# frase = "meus amigos estudantes de python"
# for i in range(len(frase)):
#     print(frase[i])

# i = 0
# while i < 10:
#     print(i)
#     i = i + 1
    
# lista = [2,1,54,6,75,23,12]
# print(lista)
# lista.sort()
# print(lista[0])
# print(lista[-1])
# print(lista)

#exemplo em que o i é um iterador sobre a lista, ou seja, ele aponta para cada elemento da lista
# for i in lista:
#     print(i)
    
# #exemplo em que o i é um índice usado para percorrer as posições de lista
# for i in range(len(lista)):
#     print(lista[i])
    
#popular uma lista com números aleatórios e mostrar o menor e o maior números
# lista = []
# for i in range(5):
#     lista.append(randint(0,100))
# print(lista)
# print(min(lista))
# print(max(lista))

#popular uma lista com n números aleatórios com controle de duplicidade
# lista = []
# n = int(input("Quantos números quer gerar? "))

# for i in range(n):
#     lista.append(i)

# print(lista)
# shuffle(lista)
# print(lista)

lista = []
for i in range(1000000):
    lista.append(randint(0,100))
    
print("Ordenação inicou")
lista.sort()
print("Processamento terminou!")