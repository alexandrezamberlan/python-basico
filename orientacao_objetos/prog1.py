class Util:
    #exemplo de método de classe - como usar static no Java
    @staticmethod
    def __teste__():
        print("chamada de método static")
    
    #exemplo de método de classe - como usar static no Java
    @staticmethod
    def __outro_metodo__(texto):
        print(texto)
        
    @staticmethod #property
    def __ordena__(lista):
        lista.sort(reverse=True)


class Pessoa:
    #construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def descobre_sobrenome(self):
        return self.nome.split()[-1]
    
    
    #equivalente a sobreescrita do equals em Java
    def __lt__(self, object):
        return self.idade < object.idade
    
    #equivalente a sobreescrita do toString em Java
    def __str__(self):
        return "%s - %s" % (self.nome, self.idade)


class Aluno(Pessoa):    #deve herdar de Pessoa e adicionar o atributo sexo no construtor
    #construtor
    def __init__(self, nome, idade, sexo):
        super().__init__(nome,idade) #chamada do método construtor do pai
        self.sexo = sexo

# a = Pessoa("Alexandre",45)
# print(a.nome)
# print(a.idade)
# print(a.descobre_sobrenome())

# aluno1 = Aluno("Gabriel Marconatto", 19, "Masculino")
# print(aluno1.descobre_sobrenome(),"  ",aluno1.sexo)


lista = []
for i in range(3):
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual a sua idade? '))
    lista.append(Pessoa(nome,idade))

# print('LISTA INICIAL')
# for i in lista:
#     print(i.nome)
#     print(i.idade)
#     print('-------')
    
    
# lista.sort(key = lambda i: i.idade, reverse=True)

Util.__ordena__(lista)

print('LISTA ORDENADA')
for i in lista:
    print(i.nome)
    print(i.idade)
    print('-------')
