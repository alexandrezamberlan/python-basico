# instruções de controle do tipo seleção
# são úteis para desviar trechos de código tendo como base uma condição

# if (condicao):
#   codigo1
#   codigo2
  
# if (condicao):
#   codigo1
#   codigo2
# else:
#   codigo3
#   codigo4


import datetime

ano = int(input("Digite um ano qualquer: "))
if (ano % 4 == 0):
  print("Ano bissexto!")
else:
  print("Ano normal")


  


data_horario_atual = datetime.datetime.now()
data = data_horario_atual.date()
ano_atual = data.strftime("%Y")
