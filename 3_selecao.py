import datetime

ano = int(input("Digite um ano qualquer: "))
if (ano % 4 == 0):
  print("Ano bissexto!")
else:
  print("Ano normal")


  


data_horario_atual = datetime.datetime.now()
data = data_horario_atual.date()
ano_atual = data.strftime("%Y")
