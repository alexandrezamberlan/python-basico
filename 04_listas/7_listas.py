#rotina que popula randomicamente uma lista (tamanho 10) com números inteiros de -100 a 100

from random import random
from random import randint

lista = []
i = 0
while (i < 10):
  #valor = random() #sorteia numeros de 0 a 1
  valor = randint(-100,100) #sorteando números entre -100 a 100
  lista.append(valor) #inserindo valor sorteado na lista
  i += 1

print("Lista gerada aleatoriamente!!")
print(lista)


#rotina que localize o menor valor da lista
menor = lista[0] #estamos assumindo que o menor é o primeiro da lista
i = 0  #incialização da variável de controle
while (i < len(lista)): #teste de parada
  if (lista[i] < menor):
    menor = lista[i]
    
  i += 1 #transformação da variável de controle

print(f"O {menor} foi o menor valor encontrado")


#rotina que localize o maior valor da lista
maior = lista[0]
i = 0  #incialização da variável de controle
while (i < len(lista)): #teste de parada
  if (lista[i] > maior):
    maior = lista[i]
    
  i += 1 #transformação da variável de controle

print(f"O {maior} foi o maior valor encontrado")


#rotina que calcule e exiba a média dos números
soma = 0
i = 0  #incialização da variável de controle
while (i < len(lista)): #teste de parada
  soma = soma + lista[i]  #acumulando item por item em soma
  i += 1

print(f"A média dos valores sorteados é {soma/len(lista)}")

#rotina que recebe um numero inteiro e exibe a sequencia dele ate 0.
numero = int(input("Digite um número: ")) 
while (numero > 0):
  print(numero)
  numero -= 1
