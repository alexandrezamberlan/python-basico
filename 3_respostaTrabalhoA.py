
# 1. Faça um Programa que peça dois números e imprima o maior deles.
numero1 = int(input('Digite um valor inteiro'))
numero2 = int(input('Digite outro valor inteiro'))

if (numero1 >= numero2):
    print(f'{numero1} é o maior ou igual')
else:
    print(f'{numero2} é o maior')

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = int(input('Digite um valor inteiro positivo ou negativo: '))

if (valor > 0):
    print(f'{valor} é positivo')
elif (valor == 0):
    print('Valor zero')
else:
    print(f'{valor} é negativo')


# 3. Faça um Programa que receba um nome completo de uma pessoa e 
# verifique se seu sobrenome contém 'Olveira'.
#    Se ocorrer 'Oliveira' imprimir "Nome contém sobrenome Oliveira", 
# caso contrário, imprimir "Nome não contém Oliveira"
nome_completo = input('Digite seu nome completo: ')
nome_completo = nome_completo.upper()

if (nome_completo.find('OLIVEIRA')):
    print('Oliveira presente no nome')
else:
    print('Oliveira ausente no nome')

# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogais = ['a', 'e', 'i','o','u','A','E','I','O','U']
numeros = ['0','1','2','3','4','5','6','7','8','9']

letra = input('Digite uma letra')
if (letra in vogais):
    print('Você digitou uma vogal')
elif letra in numeros:
    print('Você digitou um número')
else:
    print('Você digitou uma consoante')

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez. 

nota1 = float(input('Digite nota 1 [0 a 10]'))
nota2 = float(input('Digite nota 2 [0 a 10]'))
media = (nota1 + nota2)/2

if (media == 10):
    print('Aprovado com Distinção')
elif (media >= 7):
    print('Aprovado')
else:
    print('Reprovado')

# 6. Faça um Programa que leia três números e mostre o maior deles.
numero1 = int(input('Digite um valor inteiro'))
numero2 = int(input('Digite outro valor inteiro'))
numero3 = int(input('Digite terceiro valor inteiro'))

if (numero1 > numero2) and (numero2 > numero3):
    print(f'{numero1} é o maior de todos')
elif (numero2 > numero1) and (numero1 > numero3):
    print(f'{numero1} é o maior de todos')
elif (numero3 > numero1) and (numero1 > numero2):
    print(f'{numero3} é o maior de todos')


# outra solução
    
lista = []
lista.append(int(input('Digite um valor inteiro')))
lista.append(int(input('Digite outro valor inteiro')))
lista.append(int(input('Digite terceiro valor inteiro')))
print('O maior valor é: ', max(lista))


# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
lista = []
lista.append(int(input('Digite um valor inteiro')))
lista.append(int(input('Digite outro valor inteiro')))
lista.append(int(input('Digite terceiro valor inteiro')))

print('O menor valor é: ', min(lista))
print('O maior valor é: ', max(lista))

# 8. Faça um Programa que contenha uma classe Produto com os atributos descricao 
# e preco. Além disso, deve conter o método construtor
class Produto:
    descricao = ''
    preco = 0.0
    
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco

    def exibir_produto(self):
        print(self.descricao + " - " + self.preco)

prod1 = Produto('Oculos', 540)
print(prod1.preco)
print(prod1.descricao)

prod1.exibir_produto()

# 9. Faça um Programa que contenha uma classe CEP com os atributos numero, 
# cidade e estado. Além disso, deve conter o método construtor
class CEP:
    numero = 0
    cidade = ''
    estado = ''

    def __init__(self, numero, cidade, estado):
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        
        
cep_zamberlan = CEP(970160150, 'Santa Maria', 'RS')
cep_zamberlan.cidade = 'Cruz Alta'

if (cep_zamberlan.estado == 'RS'):
    print('Cep de gaúcho')

# 10. Faça um Programa que contenha uma classe Time com os atributos nome, 
# cidade, cores_principais.

class Time:
    def __init__(self, nome, cidade, cores_principais):
        self.nome = nome
        self.cidade = cidade
        self.cores = cores_principais


time1 = Time('Inter', 'Santa Maria', 'Vermelho e Branco')

times = []
times.append(time1)
times.append(Time('Grêmio','Porto Alegre', 'Azul, Branco e Preto'))






# ## Grupo B

# 1. Faça um Programa que leia dados glicêmicos de um arquivo .txt (dados um abaixo do outro) conforme o exemplo:

# 123@21/09/2021@8:12

# 89@22/09/2021@7:50
# ...


# Onde, antes do arroba é o valor da glicemia vericada, após o primeiro arroba é a data de verificação e depois do último arroba é a hora de verificação.

# O programa deve conter um Menu de operação, como o exemplo:

# Menu
# 1 - Carregar arquivo
# 2 - Listar dados glicêmicos
# 3 - Calcular e mostrar medidas centrais (média, menor e maior valor)
# 4 - Sair
# Opção: ____

# Contudo, o programa deve obrigatoriamente trabalhar com classe Glicemia(valor, data, hora), manipulação de listas e arquivos .txt.
