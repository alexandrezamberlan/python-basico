import os

lista = []
while(True):
    os.system("cls") 
    print("Menu Funcionários")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Sair")
    opcao = input("Opção: ")

    if (opcao == "1"):
        print("Cadastro de funcionário")
        #receber e validar um nome completo
        while(True):
            nome_completo = input("Informe seu nome completo: ")
            vetor_nomes = nome_completo.split(" ")
            if (len(vetor_nomes) <= 1):
                print("Você precisa digitar um nome com sobrenome")
            else:
                break

        #montar o email a partir do primeiro nome e ultimo sobrenome
        email = vetor_nomes[0]+"."+ vetor_nomes[-1]+"@ufn.edu.br"
        email = email.lower()
        
        #verificar se o email ja cadastrado na lista, se não, cadastra-lo
        if (lista.__contains__(email)):
            print("Funcionário com este email já cadastrado")
        else:
            lista.append(email)

        #manter ordenada a lista
        lista.sort()
    elif (opcao == "2"):
        print("Listagem de funcionários")
        if (len(lista) == 0):
            print("Lista vazia")
        else:
            for i in lista:
                print(i)
    elif (opcao == "3"):
        print("Exclusão de funcionários")
        if (len(lista) == 0):
            print("Lista vazia")
        else:
            email = input("Digite email a ser excluído: ")
            if (lista.__contains__(email)):
                lista.remove(email)
                print("Email removido")
            else:
                print("Email não localizado")

    elif (opcao == "4"):
        print("Obrigado por usar o programa")
        break
    else:
        print("Opção inválida!")
    
    os.system("pause")
