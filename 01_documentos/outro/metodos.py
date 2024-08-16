import os

from noticia import Noticia
from persistencia import Persistencia

class Metodos:
    @staticmethod
    def listar(lista):
        os.system('cls')
        print('LISTAGEM DAS NOTÍCIAS')
        for item in lista:
            print(item)
            print('-----------------------------------------------------')


    @staticmethod
    def cadastrar(lista, numero_noticia):
        lista_categorias = ['ESPORTE', 'POLÍTICA', 'LAZER', 'TURISMO']

        os.system('cls')

        print('CADASTRO DE NOTÍCIA')
        titulo = input('Título da notícia: ').upper()
        
        while (True):
            categoria = input('Categoria [Esporte, Política, Lazer, Turismo]: ').upper()
            if (categoria in lista_categorias):
                break
            else:
                print('Escolha uma categoria existente!')
        
        while (True):
            texto = input('Texto da notícia: ')
            if (len(texto) <= 400):
                break
            else:
                print('Excedeu os 400 caracteres de texto')

        lista_palavras_chave = []
        for i in range(1,4):
            lista_palavras_chave.append( input(f'{i}º palavra_chave: ').upper() )

        #criar o objeto noticia
        numero_noticia += 1
        noticia = Noticia(numero_noticia, titulo, categoria, texto, lista_palavras_chave)

        lista.append( noticia )
        Persistencia.gravar( noticia )

        return numero_noticia