import matplotlib.pyplot as plt

x = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
y = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

plt.title("Dados de Esportes Visualizados")
plt.xlabel("Pulso médio")
plt.ylabel("Queima calórica")

plt.plot(x, y)

plt.grid()

plt.show()