import os

from noticia import Noticia
from persistencia import Persistencia
from metodos import Metodos

lista_noticias = []

identificador_atual = Persistencia.conectar_base(lista_noticias)
if (identificador_atual > 0):
    print('Base conectada')

while (True):
    os.system("cls")
    print('MENU DE NOTÍCIAS')
    print('1 - Cadastrar')
    print('2 - Alterar')
    print('3 - Listar')
    print('4 - Remover')
    print('5 - Sair')
    opcao = input('Opção: ')

    if (opcao == '1'):
        identificador_atual = Metodos.cadastrar(lista_noticias, identificador_atual)
    elif (opcao == '2'):
        Metodos.alterar(lista_noticias)
    elif (opcao == '3'):
        Metodos.listar(lista_noticias)
    elif (opcao == '4'):
        Metodos.remover(lista_noticias)
    elif (opcao == '5'):
        break
    else:
        print('Opção inválida!!!!')

    os.system('pause')

