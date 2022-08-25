nota1 = int(input("Informe sua primeira nota: "))
nota2 = int(input("Informe sua segunda nota: "))
nota3 = int(input("Informe sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("Sua média final é: ", media)

if (media >= 7):
    print("Você está aprovado")
elif (media < 5):
    print("Você foi reprovado")
else:
    print("Você precisa fazer uma recuperação")
    
    
# altere o código para receber 5 notas
    