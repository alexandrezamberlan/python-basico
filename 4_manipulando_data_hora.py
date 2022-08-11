import datetime

data_horario_atual = datetime.datetime.now()
data = data_horario_atual.date()
hora_completa = data_horario_atual.time()

print(f"A data e hora completa é {data_horario_atual}")
print(f"A data é {data}")
print(f"A hora é {hora_completa}")

ano = data.strftime("%Y")
mes = data.strftime("%m")
dia = data.strftime("%d")

print(f"Dia atual -> {dia}")
print(f"Mês atual -> {mes}")
print(f"Ano atual -> {ano}")

hora = hora_completa.strftime("%H")
minutos = hora_completa.strftime("%M")

print(f"Hora -> {hora}")
print(f"Minutos -> {minutos}")


print("Depois de manipular data e hora..... vamos tratar idades")

nome = input("Qual seu nome? ")
nome = nome.upper()

dia_nascimento = int(input("Que dia você nasceu? "))
mes_nascimento = int(input("Que mês você nasceu? "))
ano_nascimento = int(input("Que ano você nasceu? "))


idade = int(ano) - ano_nascimento

print(f"{nome} você digitou que tem {idade} anos")
print(f"{nome}, de fato você já dormiu {idade/3:.2f} anos")

# instruções básicas
# print() - escreve algo na tela/monitor
# input() - recebe algo do usuário via o teclado
# int() - converte um texto/frase para inteiro
# float() - converte um texto/frase para float

# instruções de apoio/adicionais
# upper() - converte uma string/frase para maiúsculo

# instrução de import
# import datetime

# data_horario_atual = datetime.datetime.now()
# data = data_horario_atual.date()
# hora_completa = data_horario_atual.time()

# ano = data.strftime("%Y")
# mes = data.strftime("%m")
# dia = data.strftime("%d")

# hora = hora_completa.strftime("%H")
# minutos = hora_completa.strftime("%M")
