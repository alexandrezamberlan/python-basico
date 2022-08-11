import os

class Inflacao:
    #atributos
    valor = 0   
    mes = ""
    ano = 0
    
    meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    #método construtor não vazio, que cria um objeto ja com valores para os atributos
    def __init__(self, v, m, a):
        self.valor = v
        self.mes = m
        self.ano = a
      
    #método public para realizar um serviço  
    def mostrar_numero_mes(self):
        numero = self.meses_ano.index(self.mes)
        return numero + 1
        



os.system("clear")
mes1 = Inflacao(7.6,"Janeiro", 2022) #construir com o método construtor

print(f'O objeto mes1 tem inflação {mes1.valor}, do mês {mes1.mes} e do ano {mes1.ano}')

mes2 = Inflacao(9.4,"Fevereiro", 2022)
print(f"Número do mês {mes2.mes} é {mes2.mostrar_numero_mes()}")

lista = []
lista.append(mes1) #0
lista.append(mes2) #1
lista.append( Inflacao(4.3, "Março", 2022) ) #2

for i in lista:
    print(f'O objeto do mês {i.mes} e do ano {i.ano} tem inflação de {i.valor}%')
    
soma = 0
for i in lista:
    soma = soma + i.valor
    
media = soma / len(lista)
print(f"A média das inflações dos últimos {len(lista)} meses é de {round(media,2)}%")

