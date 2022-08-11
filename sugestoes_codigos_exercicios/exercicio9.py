#9 - Faça uma adição/complemento no código anterior para mostrar os valores de glicemia
#    da lista_dados_originais, um abaixo do outro.


lista_dados_originais = []

continuar = '1'

while (continuar == '1'):
    valor = int( input("Digite um valor de glicemia: ") )
    lista_dados_originais.append(valor)
    continuar = input("1 - Continua; Outra tecla sai: ")

for elemento in lista_dados_originais:
    print(elemento)
    