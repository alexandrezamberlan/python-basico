#8 - Faça um programa em Python que manipule listas com números inteiros, representando
#    valores de glicemia (45 a 450) de um doente diabético. O programa deve receber valores de 
#    glicemia (um a um) até que o usuário não queira mais cadastrá-los. Os dados digitados
#    devem ser inseridos na lista lista_dados_originais.


lista_dados_originais = []


while (continuar == '1'):
    valor = int( input("Digite um valor de glicemia: ") )
    lista_dados_originais.append(valor)
    continuar = input("1 - Continua; Outra tecla sai: ")


