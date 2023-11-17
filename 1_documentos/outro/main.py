import os

from noticia import Noticia
from persistencia import Persistencia

lista_noticias = []

identificador_atual = Persistencia.conectar_base(lista_noticias)
if (identificador_atual > 0):
    print('Base conectada')

while (True):
    os.system("cls")
    print('MENU DE NOTÍCIAS')
    print('1 - Cadastrar')
    print('2 - Alterar')
    print('3 - Pesquisar')
    print('4 - Remover')
    print('5 - Sair')
    opcao = input('Opção: ')

    if (opcao == '1'):
        pass
    elif (opcao == '2'):
        pass
    elif (opcao == '3'):
        pass
    elif (opcao == '4'):
        pass
    elif (opcao == '5'):
        break
    else:
        print('Opção inválida!!!!')

    os.system('pause')