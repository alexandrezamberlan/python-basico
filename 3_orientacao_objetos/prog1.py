#w3school é a referência para Python

class Pessoa:
    #construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sono(self):
        return self.idade / 3
        
        
a = Pessoa("Flavio",21)
print(a.nome)
print(a.idade)
print(a.nome," você já dormiu ", a.sono(), " anos")
 