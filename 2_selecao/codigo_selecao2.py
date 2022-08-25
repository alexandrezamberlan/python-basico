ano = int(input("Informe o ano que gostaria de verificar se é ou não bissexto: "))

if (ano % 4 == 0):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} NÃO é um ano bissexto")
    
