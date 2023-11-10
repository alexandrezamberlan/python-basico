import os

from oo1 import Veiculo
from persistencia import Persistencia

os.system("cls")

garagem = []

if (Persistencia.conectar_base(garagem)):
    print('Base conectada')

quantidade = int(input("Quantos veículos deseja cadastrar? "))

for i in range(quantidade):
    while (True):
        placa = input("Digite uma placa válida: ").upper()
        if (Veiculo.valida_placa(placa)):
            break
        else:
            print("Placa inválida....")
    
    v = Veiculo(placa)
    if (v not in garagem):
        garagem.append(v)
        Persistencia.gravar(v)
    else:
        print("Placa já cadastrada")

garagem.sort()

for i in garagem:
    print(i)