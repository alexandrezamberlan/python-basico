#fazer um programa em Python que o usuário informe quantos nomes serão cadastrados numa lista chamada meus_amigos


meus_amigos = [] #os colchetes indicam a lista
qtd_amigos = int( input("Quantos amigos quer cadastrar? ") )

i = 0
while (i < qtd_amigos): 
    nome = input("Nome de amigo: ").upper()
    
    if (not meus_amigos.__contains__(nome)): 
        meus_amigos.append(nome)
        i = i + 1
    else :
        print(f"{nome} já cadastrado!!!")


# ordenar a lista
meus_amigos.sort()

print(meus_amigos)

# for i in meus_amigos:
#     print(i)