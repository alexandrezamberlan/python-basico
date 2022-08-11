class Aluno:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
             
a = Aluno('Alex', 45)
a.nome = 'Carlos'
print(a.nome)