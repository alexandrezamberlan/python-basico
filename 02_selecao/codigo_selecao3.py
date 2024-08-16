import datetime

data_horario_atual = datetime.datetime.now()
data_atual = data_horario_atual.date()
ano_atual = int(data_atual.strftime("%Y"))
print(f"Hoje é o ano de {ano_atual}")
    

ano_nascimento = int(input("Qual seu ano de nascimento: "))
print(f"Você informou que nasceu em {ano_nascimento}")

idade = ano_atual - ano_nascimento

if (idade >= 18):
    print("Você já é adulto")
elif (idade < 12):
    print("Você é uma criança")
else:
    print("Você é um adolescente ou jovem")