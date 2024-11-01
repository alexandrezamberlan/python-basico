import os

def criar_menu(nome_arquivo, lista):
    while (True):
        os.system('cls')
        print('MENU')
        print('1 - Listar expressoes chave')
        print('2 - Cadastrar expressoes chave')
        print('3 - Analisar arquivo')
        print('4 - Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            print('Listando expressoes')            
        elif opcao == '2':
            print('Cadastrando expressoes')
        elif opcao == '3':
            print('Iniciando processo de analise em texto')
            # arquivo texto para análise das expressões
        elif opcao == '4':
            print('Deixando o sistema')
            break
        else:
            print('Opcao invalida!')

        os.system('pause')

def conectar_base(nome_arquivo, lista):
    pass

#programa principal
# lista para as expressões
lista_expressoes = []

# arquivo para as expressões
nome_arquivo_expressoes = 'expressoes.csv'



conectar_base(nome_arquivo_expressoes, lista_expressoes)
criar_menu(nome_arquivo_expressoes, lista_expressoes)
