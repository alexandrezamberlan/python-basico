lista = [4,5,6,7,3,12,0,-4]

# def exibe_lista(l):
#     print(l)
    
# def menor_valor_lista(l):
#     l.sort()
#     return l[0] 

# def maior_valor_lista(l):
#     l.sort()
#     # return l[len(l)-1]
#     return l[-1] 
    
# exibe_lista(lista)
# print(lista)
# print('Menor valor da lista é ', menor_valor_lista(lista))
# print('Maior valor da lista é ', maior_valor_lista(lista))


def retira_menor_maior_valor_lista(l):
    # l.sort()
    # l.remove(l[0])
    # l.remove(l[-1])
    l.remove(min(l))
    l.remove(max(l))
    
retira_menor_maior_valor_lista(lista)
print(lista)


def altera_numero(numero, novo_numero):
    numero = novo_numero
    return numero

numero = 9
numero = altera_numero(numero,99)
print(numero)

