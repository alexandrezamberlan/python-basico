from __future__ import with_statement

import matplotlib.pyplot as plt
import numpy as np


nome_arquivo = input("Informe nome do arquivo com dados para o gráfico: ")

dia_semana = []
valor_glicemico = []

try:
    with open(nome_arquivo,"r") as arquivo:        
        for linha in arquivo:
            # splitando a linha em lista de 2 posições
            lista_linha = linha.split(";")           
            dia_semana.append((lista_linha[0]))
            valor_glicemico.append(int(lista_linha[1]))
            
    plt.title("Medidas glicêmicas semanal")
    plt.xlabel("Dia da semana")
    plt.ylabel("Valor glicêmico")
    plt.bar(dia_semana,valor_glicemico)
    plt.show()
except:
    print("Alguma exceção foi gerada na execução do programa....")    

