#11 - Faça um complemento no código anterior para mostrar o menor e o maior valores
#     de glicemia cadastrados.

lista_dados_originais = []
lista_dados_ordenados = []

continuar = '1'

while (continuar == '1'):
    valor = int( input("Digite um valor de glicemia: ") )
    lista_dados_originais.append(valor)
    continuar = input("1 - Continua; Outra tecla sai: ")

print("Relação de valores originais: ")
for elemento in lista_dados_originais:
    print(elemento)
    

#ha duas formas para copiar o conteudo de uma lista para outra lista
#1a opcao
lista_dados_ordenados = lista_dados_originais[:] 

#2a opcao
#lista_dados_ordenados = lista_dados_originais.copy()

lista_dados_ordenados.sort()

# print("Relação de valores ordenados: ")
# for elemento in lista_dados_ordenados:
#     print(elemento)

print(f"O menor valor de glicemia cadastrado é: {lista_dados_ordenados[0]}")
print(f"O maior valor de glicemia cadastrado é: {lista_dados_ordenados[-1]}")