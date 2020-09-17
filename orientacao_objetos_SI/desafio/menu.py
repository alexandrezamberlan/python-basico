from usuario import Usuario

import os

class Menu:
    @staticmethod
    def menu(lista_usuarios, lista_atas):
        while True:
            Menu.limpar_tela()
            print("Sistema de Gestão de Atas")
            print("1 - Cadastrar usuários")
            print("2 - Atualizar usuários")
            print("3 - Listar usuários")
            print("4 - Cadastrar atas")
            print("5 - Atualizar atas")
            print("6 - Listar atas")
            print("7 - Sair")
            opcao = input("Opção: ")
            
            if opcao == '1':
                Menu.cadastrar_usuarios(lista_usuarios)
            elif opcao == '2':
                pass
            elif opcao == '3':
                pass
            elif opcao == '4':
                pass
            elif opcao == '5':
                pass
            elif opcao == '6':
                pass
            elif opcao == '7':
                Menu.limpar_tela()
                print("Obrigado por usar o sistema")
                break
            else:
                print("Opção inválida!!")
                Menu.pegar_tecla('Tecle Enter para continuar...')
                Menu.limpar_tela()
    
    @staticmethod
    def cadastrar_usuarios(lista):
        Menu.limpar_tela()
        print("Cadastro de usuários")
        # matricula, nome, tipo (leitor ou redator), email (CRUD)
        matricula = int(input('Matrícula: '))
        nome = input('Nome: ')
        nome = nome.upper()
        while True:
            t = input('R - Redator; L - Leitor: ')
            t = t.upper()
            if t == 'R':
                tipo = 'Redator'
                break
            elif t == 'L':
                tipo = 'Leitor'
                break
            else:
                print("Escolha R ou L!!")
            
        email = input('Email: ')
        lista.append(Usuario(matricula, nome, tipo, email))
        print('Usuário %s cadastrado com sucesso' % (lista[-1]))
        Menu.pegar_tecla('Tecle Enter para continuar...')
    
    
    @staticmethod
    def limpar_tela():
        os.system("clear")
        
    @staticmethod
    def pegar_tecla(texto):
        a = input(texto).split(" ")[0]
        