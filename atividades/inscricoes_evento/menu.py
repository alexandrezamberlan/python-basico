import os

from util import inscricao, conexao_base, listagem

lista_inscritos = [] #guardar a matrícula
conexao_base(lista_inscritos)

while (True):
    os.system('cls')
    print('MENU')
    print('1 - Fazer inscrições')
    print('2 - Listar inscritos')
    print('3 - Registrar entrada')
    print('4 - Registrar saída')
    print('5 - Finalizar')
    op = input('Opções: ')

    if op == '1':
        print('Inscrições')
        #chamar o metodo de inscricao
        inscricao(lista_inscritos)
    elif op == '2':
        print('Listagem de inscritos')
        #chamar o metodo de listagem
        listagem()
    elif op == '3':
        print('Entrada')
        #chamar o metodo de entrada no evento
    elif op == '4':
        print('Saída')
        #chamar o metodo de saida do evento
    elif op == '5':
        print('Obrigado por usar o sistema')
        break
    else:
        print('Opção inválida!')

    os.system('pause')
