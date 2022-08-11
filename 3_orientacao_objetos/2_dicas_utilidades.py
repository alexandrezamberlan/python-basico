# importando o pacote os - contém métodos ou serviços para comunicar com o SO da máquina
import os 

os.system("clear")



# usando o split de classe string
nome_completo = 'Diogo Sihe Balconi'
nomes = nome_completo.split(' ')
print(nomes[0])
print(nomes[-1])



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

inflacao_vigente = "6.7;janeiro;2021"
dados = inflacao_vigente.split(';')

inflacao = Inflacao(dados[0], dados[1], dados[2])

print(f'A inflacao vigente {inflacao.mes} de {inflacao.ano} é de {inflacao.valor}%')
