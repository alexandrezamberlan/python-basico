import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Seg", "Ter", "Qua", "Qui", "Sex"])
y = np.array([12, 11, 9, 8, 13])


plt.title("Consumo semanal combustível")
plt.xlabel("Dia da semana")
plt.ylabel("Média consumo por km/l")
plt.bar(x,y)
plt.show()