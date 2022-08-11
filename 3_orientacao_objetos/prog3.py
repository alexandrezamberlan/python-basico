#w3school é a referência para Python

from random import randint

class Util:
    @staticmethod
    def __popular__(lista, quantidade):
        
        for i in range(quantidade):
            matricula = int(input("Matrícula: "))
            nome = input("Nome: ")
            idade = input("Idade: ")
            lista.append(Aluno(matricula, nome, idade))
    
    @staticmethod            
    def __exibir__(lista):
        for i in lista:
            print(i)
            
    #criar na classe Util um método estático que retorne o aluno mais novo

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
 
    #sobreescrevendo o toString do python
    def __str__(self):
        return "Nome: " + self.nome + " - Idade: " + str(self.idade) + " - Matrícula: " + str(self.matricula)
        
    
lista = []
quantidade = int(input("Quantos alunos quer cadastrar? "))
Util.__popular__(lista, quantidade)
Util.__exibir__(lista)
