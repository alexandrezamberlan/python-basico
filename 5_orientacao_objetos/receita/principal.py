from receita import Receita
from tipo import Tipo

sobremesa = Tipo("Sobremesa", "Doce")

receita1 = Receita("Quindim", sobremesa)
receita1.informar_ingredientes()

print(receita1.titulo)
print(receita1.tipo.descricao)
receita1.mostrar_ingredientes()
