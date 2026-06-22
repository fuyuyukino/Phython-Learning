import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 4, 6, 8, 10, 12, 14])
ypoints = np.array([18, 4, 12, 8, 4, 25, 18, 21])

plt.plot(xpoints, ypoints,"o--c", ms = 12, mec = "y")
plt.show()