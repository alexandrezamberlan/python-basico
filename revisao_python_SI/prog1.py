#um comentário de uma linha

"""
comentários que ocupam 
mais de uma linha
"""

print("Oi turma de python-django")
print("Meu nome é Alexandre 'Croco' Zamberlan")

#variáveis no Python, é dito NÃO TIPADAS, exceto quando são Objetos de uma classe

nome = input("Digite seu nome: ")
idade = int(input("Qual a sua idade? "))
print(nome," você já dormiu ", idade/3, " anos")

if (idade >= 18 and idade <= 60):
    print(nome, " você é considerado cidadão ativo!!")
    sexo = input("Qual seu sexo? [M ou F]")
elif idade < 18:
    print("Você é considerado de menor")
    responsavel = input("Qual o nome do seu/sua responsável?")
else:
    print("Você chegou na melhor idade!")
    