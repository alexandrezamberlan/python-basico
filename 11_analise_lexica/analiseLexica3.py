import os

def atualizar_base(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as escritor:
        for item in lista:
            escritor.write(item + '\n')

def listar(lista):
    contador = 0
    for item in lista:
        contador += 1
        print(item)
    print('-----------------')
    print('Total: ', contador)

def cadastrar(lista, nome_arquivo):
    expressao = input('Digite expressão a ser cadastrada: ').upper()
    if expressao not in lista:
        lista.append(expressao)
        lista.sort()
        atualizar_base(lista, nome_arquivo)
    else:
        print('Expressao ja cadastrada')
    

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
            listar(lista)        
        elif opcao == '2':
            print('Cadastrando expressoes')
            cadastrar(lista, nome_arquivo)
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
    #associar o nome_arquivo com uma variavel procuradora
    with open(nome_arquivo, 'r') as leitor:
        #percorrer a variavel procuradora e capturar as expressoes e inseri-las na lista
        for linha in leitor:
            # Aqui você pode analisar cada linha
            linha = linha.strip()  # Remove espaços em branco no início e no final
            lista.append(linha.upper())

#programa principal
# lista para as expressões
lista_expressoes = []

# arquivo para as expressões
nome_arquivo_expressoes = 'expressoes.csv'

conectar_base(nome_arquivo_expressoes, lista_expressoes)
criar_menu(nome_arquivo_expressoes, lista_expressoes)
