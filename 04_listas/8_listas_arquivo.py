nome_arquivo = input("Qual o nome do arquivo que deseja abrir? ")
arquivo = open(nome_arquivo, "r")
conteudo = arquivo.read()

minha_lista = conteudo.split("\n")

# convertendo a lista, um por um, de str para inteiro
for i in range(0, len(minha_lista)):
    minha_lista[i] = int(minha_lista[i])

arquivo.close()
minha_lista.sort()
print(minha_lista)

print(minha_lista[0])
print(minha_lista[-1])

media = 0
soma = 0
for i in minha_lista:
    soma = soma + i
    
media = soma / len(minha_lista)
print(media)