# programa em python que lê um arquivo fonte.dat com dados de inflação (valor, mes e ano separados por @)
# os dados vindos do arquivo são inseridos em uma lista

from __future__ import with_statement

#try - except: é um recurso das linguagens de programação para capturar e tratar exceções/erros gerados na execução

#with: é um recurso de Python para abrir arquivos e garantir que sejam fechados automaticamente


nome_arquivo = input("Informe nome do arquivo com dados de inflação do período: ")

try:
    lista_inflacao = []
    with open(nome_arquivo,"r") as arquivo:
        print("Arquivo localizado! ")
        for linha in arquivo:
            # print(linha)
            # splitando a linha em lista de 3 posições
            lista_linha = linha.split("@")
            # print(lista_linha[0])
            # adicionando so a inflacao na lista de inflacao
            lista_inflacao.append(float(lista_linha[0]))
            
    # depois de abrir arquivo, retirar dados de inflacao e inseri-los na lista, vamos exibi-los
    for i in lista_inflacao:
        print(i)
        
    #vamos copiar a lista para uma lista que será ordenada 
    lista_inflacao_ordenada = lista_inflacao[:]
    lista_inflacao_ordenada.sort()
    
    #mostrar o menor índice de inflação do período
    print(f"O menor valor da inflação do perído foi {lista_inflacao_ordenada[0]}")
    
    #mostrar o maior índice de inflação do período
    print(f"O maior valor da inflação do perído foi {lista_inflacao_ordenada[-1]}")
    
    #calcular e mostar a média de inflação do período
    soma = 0
    for i in lista_inflacao:
        soma = soma + i

    media = soma / len(lista_inflacao)
    print(f"O média da inflação do perído foi {round(media,2)}")            
        
        
except:
    print("Alguma exceção foi gerada na execução do programa....")    