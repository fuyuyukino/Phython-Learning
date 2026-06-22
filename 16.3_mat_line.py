import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([20, 30, 25, 30, 40])
x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([12, 25, 35, 20, 50])

plt.plot(x1, y1, ":", c = "hotpink", lw = 2)
plt.plot(x2, y2, ":", c = "cyan", lw = 2)
plt.show()