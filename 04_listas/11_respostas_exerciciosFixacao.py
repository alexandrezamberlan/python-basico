numeros_inteiros = []

while (True) :
    valor = int(input("Digite um número inteiro: "))
    if (not numeros_inteiros.__contains__(valor)):
        numeros_inteiros.append(valor)
    else:
        print("Número já cadastrado")
    
    op = input("1 - Continua; 2 ou outra tecla termina: ")
    if (op != '1'):
        break

numeros_inteiros.sort()

# exibe toda a lista, numa tacada só
print(numeros_inteiros)

# exibe toda a lista, um valor por vez
for i in numeros_inteiros:
    print(i)
    
tamanho_lista = len(numeros_inteiros)
meio_lista = int(tamanho_lista / 2)

print(f"O meio da lista é o número: {numeros_inteiros[meio_lista]}")