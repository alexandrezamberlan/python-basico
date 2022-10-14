from __future__ import with_statement

class Pessoa:
    def __init__(self, nome, email, matricula):
        self.nome = nome
        self.email = email
        self.matricula = matricula

    def primeiro_nome(self):
        nomes = self.nome.split(" ")
        return nomes[0]        
    
    def sobrenome(self):
        nomes = self.nome.split(" ")
        return nomes[-1]        
    
    
lista_inscritos = []
nome_arquivo_inscritos = "inscritos.csv"

while (True):
    print("MENU")
    print("1 - Realizar inscrição")
    print("2 - Listar inscritos")
    print("3 - Sair")
    opcao = int(input("Opção: "))

    if (opcao == 1):
        print("INSCRIÇÃO")
        
        
    elif (opcao == 2):
        print("LISTAGEM INSCRITOS")
        
    elif (opcao == 3):
        print("Obrigado por usar o sistema")
        break
    else:
        print("Opção inválida!")

