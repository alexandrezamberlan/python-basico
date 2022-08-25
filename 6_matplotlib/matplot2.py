import matplotlib
import matplotlib.pyplot as plt
import random


sistolica = []  #pressao maxima 50 a 200 - eixo y
diastolica = [] #pressao minima 10 a 30 - eixo x

for i in range(0,23):
    sistolica.append(random.randrange(50,200))
    diastolica.append(random.randrange(10,30))

plt.title("Pressão arterial")
plt.xlabel("pressão diastólica")
plt.ylabel("pressão sistólica")

plt.scatter(diastolica, sistolica)
plt.show()