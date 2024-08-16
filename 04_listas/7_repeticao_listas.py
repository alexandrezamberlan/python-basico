# Foco da aula é usar a estrutura de dados List do Python e instruções de repetição para armazenar, consultar dados

meus_alunos = [] #foi declarada uma variável meus_alunos do tipo lista

#o comando append() associado a uma lista, insere no fim um valor na lista
meus_alunos.append("Diogo") #0
meus_alunos.append("Vitor") #1
meus_alunos.append("Clara") #2
meus_alunos.append("Dante") #3
meus_alunos.append("Tales") #4

# meus_alunos.append(234) #cuidado, pois a lista é genérica

print("Exibindo a lista inteira!")
print(meus_alunos)


#alternativa 1 para exibir os elementos de uma lista
print("Exibindo um elemento por vez da lista de tamanho ", len(meus_alunos))
# i = 0 #nessa alternativa, o i é um número que indica a posição na lista
# while (i < len(meus_alunos)):  #comando len() retorna o comprimento de uma lista ou string
#     print(meus_alunos[i])
#     i = i + 1

#alternativa 2 para exibir os elementos de uma lista
for i in meus_alunos: #nessa alternativa, o i é um ponteiro
    print(i)


nome = input("Digite um nome para pesquisa: ")

localizado = False #variavel booleana, que vai ter ou True (verdade) ou False (falso)

for i in meus_alunos: #nessa alternativa, o i é um ponteiro
    if (nome.upper() == i.upper()):
        print(f"{nome} está na lista")
        localizado = True
        
if localizado == False:
    print(f"{nome} não localizado!")
