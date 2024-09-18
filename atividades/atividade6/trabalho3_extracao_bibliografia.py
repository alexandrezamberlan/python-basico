#menu de opções para o usuário escolher o que fazer

# Menu
# 1 - Mostrar arquivo de bibliografia
# 2 - Listar os autores
# 3 - Listar o principal autor (ocorrencia)
# 4 - Sair
# Opção: 

# Estruturas de dados necessárias
# 1 - classe do tipo autor: nome, sobrenome e ocorrencias
# 2 - lista []
# 3 - with open(nome_arquivo,"r") as procurador:
# 4 - método split()
from __future__ import with_statement

class Autor:

    def __init__(self, nome, sobrenome, ocorrencias):
        self.nome = nome
        self.sobrenome = sobrenome 
        self.ocorrencias = ocorrencias

lista_autores = []
while (True):
    print("MENU")
    print("1 - Mostrar arquivo de bibliografia")
    print("2 - Listar os autores")
    print("3 - Listar o principal autor (ocorrencia)")
    print("4 - Sair")
    opcao = int(input("Opção: "))

    if (opcao == 1):
        print("Exibindo a bibliografia")
        nome_arquivo = input("Digite nome do arquivo da bibliografia: ")
        try:
            with open(nome_arquivo,"r", encoding='utf8') as procurador:
                for linha in procurador:
                    if (not linha[0] == '#'):
                        print(linha)
        except:
            print("Problemas com o arquivo ou arquivo inexistente")
    elif (opcao == 2):
        print("Exibindo autores")
        nome_arquivo = input("Digite nome do arquivo da bibliografia: ")
        try:
            with open(nome_arquivo,"r", encoding='utf8') as procurador:
                for linha in procurador:
                    if (not linha[0] == '#'):
                        dados_linha = linha.split('. ')
                        autores = dados_linha[0].split('.;') 
                        for elemento in autores:
                            if (not elemento.strip() in lista_autores):
                                lista_autores.append(elemento.strip())

                for autor in lista_autores:
                    print(autor)
        except:
            print("Problemas com o arquivo ou arquivo inexistente")

    elif (opcao == 3):
        print("Exibindo principal autor")

    elif (opcao == 4):
        print("Obrigado por usar o sistema")
        break
    else:
        print("Opção inválida!")

