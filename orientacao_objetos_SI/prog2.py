#w3school é a referência para Python

class Pessoa:
    #construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sono(self):
        return self.idade / 3


class Aluno(Pessoa):
    #construtor
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        # Pessoa.__init__(nome, idade)
        super().__init__(nome, idade)
    
    
a = Aluno(1234,"Flavio",21)
print(a.nome)
print(a.matricula)
print(a.idade)
print(a.nome," você já dormiu ", a.sono(), " anos")
 