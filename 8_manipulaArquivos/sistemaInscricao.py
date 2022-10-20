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
    


#metodo do programa principal
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
    print("MENU")
    print("1 - Realizar inscrição")
    print("2 - Listar inscritos")
    print("3 - Sair")
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
        
        #grava na lista
        lista_inscritos.append(pessoa)
        
        #grava no arquivo
        try:
            with open(nome_arquivo_inscritos, "a", encoding='utf8') as procurador:
                linha = nome + ";" + email + ";" + matricula + "\n"
                procurador.write(linha)

        except:
            print("Problemas para gravar a inscrição no arquivo!")
        
    elif (opcao == 2):
        print("LISTAGEM INSCRITOS")
        for pessoa in lista_inscritos:
            print("Matrícula: ", pessoa.matricula)
            print("Nome: ", pessoa.nome)
            print("________________________")
        
    elif (opcao == 3):
        print("Obrigado por usar o sistema")
        break
    else:
        print("Opção inválida!")

