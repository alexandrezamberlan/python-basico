#12 - Faça um complemento no código anterior para mostrar a média dos valores de 
#     glicemia cadastros e na sequência contar e mostrar quantos valores estão abaixo e
#     acima da média.

lista_dados_originais = []

continuar = '1'

while (continuar == '1'):
    valor = int( input("Digite um valor de glicemia: ") )
    lista_dados_originais.append(valor)
    continuar = input("1 - Continua; Outra tecla sai: ")

print("Relação de valores originais: ")
for elemento in lista_dados_originais:
    print(elemento)
    

soma = 0
for elemento in lista_dados_originais:
    soma = soma + elemento
    
#função len() retorna o tamanho de uma lista passada no parâmetro
media = soma / len(lista_dados_originais)

print(f"A média dos valores glicêmicos é {media}")

quantidade_acima_media = 0
quantidade_abaixo_media = 0
for elemento in lista_dados_originais:
    if (elemento < media):
        quantidade_abaixo_media = quantidade_abaixo_media + 1
    else:
        quantidade_acima_media = quantidade_acima_media + 1

# len(lista_dados_originais) ---> 100
# quantidade_abaixo_media    ---> porcentagem_abaixo_media

porcentagem_abaixo_media = (100 * quantidade_abaixo_media) / len(lista_dados_originais)
porcentagem_acima_media = 100 - porcentagem_abaixo_media

print(f"A quantidade de elementos abaixo da média é {quantidade_abaixo_media}")
print(f"A quantidade de elementos acima da média é {quantidade_acima_media}")


print(f"A porcentagem de elementos abaixo da média é {porcentagem_abaixo_media}%")
print(f"A porcentagem de elementos acima da média é {porcentagem_acima_media}%")