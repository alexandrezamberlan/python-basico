# INSTRUÇÃO WHILE
#  https://www.w3schools.com/python/python_while_loops.asp

# Instrução de repetição é uma instrução de controle: a partir de uma condição, um bloco pode executar n vezes

# TODA REPETIÇÃO OBEDECE 3 SITUAÇÕES:
  # A - inicialização da variável de controle
  # B - transformação da variável de controle
  # C - uso da variável de controle na condição de parada/continuação

# i = 1          #A - contador
# while i < 6:   #C
#   print(i)
#   i += 1       #B


# #sugestão clássica
# numero = -1                                                    #A
# while (numero < 0):                                            #C
#   numero = int(input("Digite um numero inteiro e positivo"))   #B
#   if (numero < 0):
#     print("Número inválido. Preste atenção na solicitação!")

# #sugestão alternativa
# while (True):
#   numero = int(input("Digite um numero inteiro e positivo"))  
#   if (numero < 0):
#     print("Número inválido. Preste atenção na solicitação!")
#   else:
#     break  #um comando para sair ou pular da repetição
    

# #sugestão clássica
# valor_glicose = 20
# while (valor_glicose < 30 or valor_glicose > 800):
#   valor_glicose = int(input("Digite um valor válido para a glicose em jejum: "))
#   if (valor_glicose < 30 or valor_glicose > 800):
#     print("O valor da glicose está inválido. Atenção!")


# #sugestão alternativa
# while (True):
#   valor_glicose = int(input("Digite um valor válido para a glicose em jejum: "))
#   if (valor_glicose < 30 or valor_glicose > 800):
#     print("O valor da glicose está inválido. Atenção!")
#   else:
#     break

# while (True):
#   nome_completo = input("Digite seu nome completo: ") # alexandre zamberlan
#   nome_completo = nome_completo.title()
#   lista_nomes = nome_completo.split(" ")              #[alexandre, zamberlan]
#   if (len(lista_nomes) <= 1):
#     print("Você não digitou um nome completo. Atenção!")
#   else:
#       break

# print("Você digitou ok: ", nome_completo)

# email = input("Digite seu email: ") #pedro.veio.bagual@ufn.edu.br
# lista = email.split("@")            #[pedro.veio.bagual, ufn.edu.br]
# print("usuario: ", lista[0])
# print("dominio: ", lista[1])

# while (True):
#   data = input("Digite uma data [dd/mm/aaaa]: ")  #29/09/2022
#   lista = data.split("/")                         #[29, 09, 2022]
  
#   if (len(data) != 10 or len(lista) != 3 or int(lista[0]) < 1 or 
#       int(lista[0]) > 31 or int(lista[1]) < 1 or int(lista[1]) > 12):                     #len vem de length - contar os elementos/caracter
#     print("A data está errada. Redigite!")
#   else:
#     break

# print("Dia: ", lista[0])
# print("Mês: ", lista[1])
# print("Ano: ", lista[2])

# print("Você digitou: ", data)

# FPS, MOBA, RPG, RTS, 
lista_categorias_jogos = []

#rotina que recebe do usuário as categorias, controlando as duplicadas
while (True):
  categoria = input("Digite categoria de jogo ou sair para finalizar: ")
  categoria = categoria.upper()
  if (categoria == "SAIR"):
    break
  if (categoria in lista_categorias_jogos):
    print("Categoria já cadastrada!")
  else:
    lista_categorias_jogos.append(categoria) #[FPS, RPG, RTS]

#rotina que ordena a lista de forma crescente
lista_categorias_jogos.sort()
print("\nCategorias cadastradas:")
#[FPS, RPG, RTS]
for item in lista_categorias_jogos:
  print(item)


















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

# quantidade_notas = int(input("Digite quantas notas irá cadastrar: "))
# i = 0
# soma = 0
# while (i < quantidade_notas):
#   nota = -1 #forçando para que entre no proximo while
#   while (nota < 0 or nota > 10):
#     nota = float(input(f"Digite a sua {i+1}ª nota [0 a 10]: "))
  
#   soma = soma + nota
#   i += 1

# print(f"A média das notas é {soma/quantidade_notas}")


  
# INSTRUÇÃO FOR
# https://www.w3schools.com/python/python_for_loops.asp
