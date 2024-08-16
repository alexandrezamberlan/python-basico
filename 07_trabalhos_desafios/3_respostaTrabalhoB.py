from __future__ import with_statement

#elementos da lista devem ser da classe Glicemia (mesmo arquivo ou arquivos separados)
class Glicemia:
    def __init__(self, valor_glicemia, data_medicao, hora_medicao):
        self.valor_glicemia = valor_glicemia
        self.data_medicao = data_medicao
        self.hora_medicao = hora_medicao

    def alerta(self):
        if self.valor_glicemia < 70:
            return "Atenção.... entrando em hipoglicemia..... como algo"
        elif self.valor_glicemia > 180:
            return "Atenção.... entrando em hiperglicemia..... use insulina"
        else:
            return "Glicemia normal"

#pedir para o usuario o nome do arquivo contendo os dados glicemicos
nome_arquivo = input("Digite nome do arquivo: ")

#lista de dados glicemicos
lista_glicemica = []

#abrindo um arquivo no modo leitura e o responsável é o procurador

try:
    with open(nome_arquivo,"r") as procurador:
        #percorrer o arquivo, para cada linha do arquivo splitar pelo simbolo ";" em objetos Glicemia,
        #adicionando na lista
        #para cada linha do procurador, seu conteúdo é exibido na tela
        for linha in procurador:
            dados_linha = linha.split(";")
            lista_glicemica.append(Glicemia(int(dados_linha[0]), dados_linha[1], dados_linha[2]))
except:
    print("Problemas com o arquivo")

#percorrendo a lista, item por item e exibindo....
for item in lista_glicemica:
    print(item.valor_glicemia, " ", item.alerta())

#aplicar na lista as medidas centrais: media, maior, menor valor
soma = 0
for item in lista_glicemica:
    soma = soma + item.valor_glicemia

media = soma / len(lista_glicemica)
print("A média glicêmica é: ", round(media, 1))


menor_glicemia = min(lista_glicemica, key = lambda g : g.valor_glicemia)
maior_glicemia = max(lista_glicemica, key = lambda g : g.valor_glicemia)

print("O menor valor glicêmico é: ", menor_glicemia.valor_glicemia, "  ", menor_glicemia.data_medicao)
print("O maior valor glicêmico é: ", maior_glicemia.valor_glicemia, "  ", maior_glicemia.data_medicao)