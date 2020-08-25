print('exibindo i de 0 a 9')
for i in range(10):
    print(i)

print('exibindo i de 5 a 9')
for i in range(5,10):
    print(i)
    
lista = [5,2,1,8,8,1,10,7,14]
# print(lista)

#iterando na lista com o objeto i, em que o i é um elemento por vez da lista
for i in lista:
    print(i)
  
#iterando na lista com a variável i, em que i é um índice na lista  
for i in range(len(lista)):
    print(lista[i])
    