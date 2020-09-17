#Todas a partir da data 07/08/2019
#__gte = maior ou igual que
# __gt = maior que
data_referencia = datetime(2019,7,8) #08/07/2019 00:00:00
respostas = RespostaEnquete.objects.filter(data_hora__gte=data_referencia)


#Todas até a data 07/08/2019
#__lte = maior ou igual que
# __lt = maior que
data_referencia = datetime(2019,7,8) #08/07/2019 00:00:00
respostas = RespostaEnquete.objects.filter(data_hora__lte=data_referencia)


#Todas dentro de um período 08/06/2019 00:00:00 até 08/07/2019 23:59:59 (Trinta dias de diferença)
data_final = datetime(2019,7,8,23,59,59)
data_inicial = data_final - timedelta(days=30)
respostas = RespostaEnquete.objects.filter(data_hora__range=(data_inicial,data_final))
não testei o código, mas está bem dentro do escopo do projeto de avaliação
lembrando que aí no código eu setei a data no braço, mas poderá vir de um formulário de busca... 
num campo já de DateTimeField assim já estará no formato data e hora