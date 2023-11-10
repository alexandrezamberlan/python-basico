from oo1 import Veiculo

class Persistencia:
    
    @staticmethod
    def gravar(v):
        print(v)
        try:
            with open("veiculos.csv", "a", encoding='utf8') as escritor:
                escritor.write(v.placa + ";" + v.data_entrada + ";" + v.hora_entrada)
        except:
            pass

    @staticmethod
    def conectar_base(lista):
        try:
            with open("veiculos.csv", "r", encoding='utf8') as leitor:
                for linha in leitor:
                    dados_linha = linha.split(';')
                    veiculo = Veiculo(dados_linha[0], dados_linha[1], dados_linha[2])
                    lista.append(veiculo)
                    return True
        except:
            pass
        return False