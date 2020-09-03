#w3school é a referência para Python

from random import randint

class Util:
    @staticmethod
    def __popular__(lista, quantidade):
        
        for i in range(quantidade):
            matricula = int(input("Matrícula: "))
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            lista.append(Aluno(matricula, nome, idade))
    
    @staticmethod            
    def __exibir__(lista):
        for i in lista:
            print(i)
            
    #criar na classe Util um método estático que retorne o aluno mais novo
    @staticmethod
    def __descobre_mais_novo__(lista):
        menor = lista[0]
        for i in lista:
            if (i.idade < menor.idade):
                menor = i
        
        return menor


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
    
    #sobreescrevendo o equivalente ao equals do java
    def __lt__(self, object):
        return self.idade < object.idade
        
        
    
lista = []
quantidade = int(input("Quantos alunos quer cadastrar? "))
Util.__popular__(lista, quantidade)
Util.__exibir__(lista)
print("O aluno mais novo é ", Util.__descobre_mais_novo__(lista))
# lista.sort()
# print("Exibindo ordenada por idade")
# Util.__exibir__(lista)




