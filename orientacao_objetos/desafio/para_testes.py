#from .usuario import Usuario -> para pycham
from usuario import Usuario # para vscode
from ata import Ata

u = Usuario(1234,"Mariano", "Redator", "mariano@ufn.edu.br")
ata1 = Ata(1, "10/09/2020", "19:00", "Teams da disciplina", "Orientação a objetos em Python")
print("Ata1  ", ata1)
ata1.redator = u
print("Redator ata1 ", ata1.redator)

for i in range(2):
    matricula = int(input("Matricula: "))
    nome = input("Nome: ")
    nome = nome.upper()
    tipo = input("Tipo (Redator ou Leitor): ")
    tipo = tipo.upper()
    email = input("Email: ")
    ata1.lista_integrantes.append(Usuario(matricula,nome,tipo,email))

# print(ata1.lista_integrantes)

for i in ata1.lista_integrantes:
    print(i)


# ata2 = Ata(2, "10/09/2020", "20:00", "Teams da disciplina", "Framework Django")
# ata2.redator = Usuario(2344,"Eduardo","Redator", "dudu@ufn.edu.br")

# print("Ata2 ", ata2)
# print("Redator ata2 ", ata2.redator)

