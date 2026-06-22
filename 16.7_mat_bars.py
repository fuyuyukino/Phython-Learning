import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(["A", "B", "C", "D"])
ypoints = np.array([10, 20, 15, 25])

plt.bar(xpoints, ypoints, width = 0.3)
plt.show()