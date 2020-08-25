lista = [4,5,6,7,3,12,0,-4]

def exibe_lista(l):
    print(l)
    
def menor_valor_lista(l):
    l.sort()
    return l[0] 

def maior_valor_lista(l):
    l.sort()
    # return l[len(l)-1]
    return l[-1] 
    
exibe_lista(lista)
print(lista)
print('Menor valor da lista é ', menor_valor_lista(lista))
print('Maior valor da lista é ', maior_valor_lista(lista))

retira_menor_maior_valor_lista(lista)
print(lista)