import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

xpoints = np.array([0, 3, 6])
ypoints = np.array([0, 100, 250])

plt.plot(xpoints, ypoints)
plt.show()