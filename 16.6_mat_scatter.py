from ast import Module
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.random.randint(100, size=(100))
ypoints = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 5 * np.random.randint(100, size=(100))
plt.scatter(xpoints, ypoints, c = colors, s = sizes, alpha = 0.5, cmap='spring')
plt.colorbar()
plt.show()