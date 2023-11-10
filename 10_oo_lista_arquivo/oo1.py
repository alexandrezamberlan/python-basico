# Programação profissional
#     - Teoria da Orientação a Objetos
#         - encapsulamento e visibilidade
#         - herança
#         - polimorfismo

#     - Na prática a OO
#         - terceirização de serviços
#         - classe == categoria == tipo
#             - geradora de objetos (molde)
#             - composta:
#                 - atributos == variáveis
#                 - métodos == operações
#         - objeto é um exemplo, ou instância de uma classe


import datetime

class Veiculo:
    
    # construtor
    def __init__(self, placa):
        self.placa = placa
        self.data_entrada = datetime.datetime.now().date()
        self.data_saida = ''
        self.hora_entrada = datetime.datetime.now().time()
        self.hora_saida = ''
        self.valor_cobrado = 0

    def __str__(self):
        return f"Veículo: {self.placa}. Entrada: {self.data_entrada} - {self.hora_entrada}"
    
    def __eq__(self, other):
        if isinstance(other, Veiculo):
            return self.placa == other.placa
        return False

    def __gt__(self, other):
        return self.placa > other.placa
        

    @staticmethod
    def valida_placa(placa):
        if (len(placa) != 7):
            return False 
        return True