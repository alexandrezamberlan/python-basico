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
