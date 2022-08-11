# INSTRUÇÃO WHILE
#  https://www.w3schools.com/python/python_while_loops.asp

# TODA REPETIÇÃO OBEDECE 3 SITUAÇÕES:
  # A - inicialização da variável de controle
  # B - transformação da variável de controle
  # C - uso da variável de controle na condição de parada/continuação

i = 1          #A
while i < 6:   #C
  print(i)
  i += 1       #B

  
# rotina que exibe o i de 1 a 5
# i = 1   #inicialização da variável de controle.
# while (i < 6): #uso da variável de controle na condição de parada.
#   #conjunto de código que quer repetir 5 vezes
#   print(f"repetindo a {i}ª vez")
#   i += 1  #transformação da variável de controle.


# rotina que recebe nomes de pessoas (convertidas em maiúsculo),
# inseridas no final da lista, enquanto o usuário desejar repetir
# lista = []  
# opcao = '1'
# while (opcao == '1'):
#   nome = input("Digite seu nome: ")
#   lista.append(nome.upper())
#   opcao = input("Digite 1 para continuar; qualquer tecla para sair: ")

# print(lista)


# rotina que cadastra qtd amigos na lista meus_amigos
# qtd = int(input("Quantos amigos quer cadastrar? "))
# i = 0
# meus_amigos = []
# while (i < qtd):
#   nome = input("Digite o nome de um amigo: ")
#   meus_amigos.append(nome)
#   i += 1
# print(meus_amigos)


#rotina que recebe do usuario quantas notas ele deve informar e recebe os valores das notas (0 a 10), sempre repetindo as notas invalidas. Ao final, deve mostrar a média dessas notas

quantidade_notas = int(input("Digite quantas notas irá cadastrar: "))
i = 0
soma = 0
while (i < quantidade_notas):
  nota = -1 #forçando para que entre no proximo while
  while (nota < 0 or nota > 10):
    nota = float(input(f"Digite a sua {i+1}ª nota [0 a 10]: "))
  
  soma = soma + nota
  i += 1

print(f"A média das notas é {soma/quantidade_notas}")


  
# INSTRUÇÃO FOR
# https://www.w3schools.com/python/python_for_loops.asp
