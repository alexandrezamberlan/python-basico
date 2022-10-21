from __future__ import with_statement

import os

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
    


#metodos do programa principal
def valida_nome_completo(nome):
    nomes = nome.split(" ")
    if (len(nomes) <= 1):
        return False
    else:
        return True
    
def valida_email(email):
    if (not email.__contains__("@") or len(email) < 10):
        return False
    return True

def jaCadastrado(matricula, lista):
    for pessoa in lista:
        if (matricula == pessoa.matricula):
            return True
    return False


lista_inscritos = []
nome_arquivo_inscritos = ".\8_manipulaArquivos\inscritos.csv"

#abrir o arquivo de inscritos.csv e popular a lista_inscritos
try:
    with open(nome_arquivo_inscritos, "r", encoding='utf8') as procurador:
        for linha in procurador:
            dados_linha = linha.split(';')
            pessoa = Pessoa(dados_linha[0], dados_linha[1], dados_linha[2])
            lista_inscritos.append(pessoa)
        print("Base de dados conectada....")
except:
    pass


while (True):
    os.system("cls")
    print("MENU")
    print("1 - Realizar inscrição")
    print("2 - Listar inscritos")
    print("3 - Remover inscrito")
    print("4 - Sair")
    opcao = int(input("Opção: "))

    if (opcao == 1):
        print("INSCRIÇÃO")
        while (True):
            nome = input("Digite nome completo: ").upper()
            if (valida_nome_completo(nome) == True):
                break               
        
        while (True):
            email = input("Digite email da pessoa: ")
            if (valida_email(email) == True):
                break
        
        while (True):
            matricula = input("Digite a matrícula da pessoa: ")
            if (len(matricula) >= 5):
                break
            
        pessoa = Pessoa(nome,email,matricula)
        
        #grava na lista se a matrícula não estiver lá
        if (jaCadastrado(matricula, lista_inscritos)):
            print("Esta pessoa com esta matrícula já está inscrita")
        else:
            #granva na lista
            lista_inscritos.append(pessoa)
            #grava no arquivo
            try:
                with open(nome_arquivo_inscritos, "a", encoding='utf8') as procurador:
                    linha = nome + ";" + email + ";" + matricula + ";\n"
                    procurador.write(linha)
            except:
                print("Problemas para gravar a inscrição no arquivo!")
            
    elif (opcao == 2):
        print("LISTAGEM INSCRITOS\n")
        for pessoa in lista_inscritos:
            print("Matrícula: ", pessoa.matricula)
            print("Nome: ", pessoa.nome)
            print("________________________")
    
    elif (opcao == 3):
        print("REMOÇÃO DE INSCRITO\n")
        matricula = input("Informe matrícula a ser removida: ")

        for pessoa in lista_inscritos:
            if (matricula == pessoa.matricula):
                #remover da lista
                lista_inscritos.remove(pessoa)                               
                print("Remoção realizada com sucesso")
                break
        
        #atualizar o arquivo com a nova lista
        try:
            with open(nome_arquivo_inscritos, "w", encoding='utf8') as procurador:
                for pessoa in lista_inscritos:
                    linha = pessoa.nome + ";" + pessoa.email + ";" + pessoa.matricula + ";\n"
                    procurador.write(linha)
        except:
            print("Problemas para gravar a inscrição no arquivo!")
    

    elif (opcao == 4):
        print("Obrigado por usar o sistema")
        break
    else:
        print("Opção inválida!")
    
    os.system("pause")

