import matplotlib.pyplot as plt
import numpy as np

#Plot 1
xpoints = np.array([1, 2, 3])
ypoints = np.array([1, 2, 3])

plt.subplot(2,2,1)
plt.plot(xpoints, ypoints)
plt.title("COMPANY 1")

#Plot 2
xpoints = np.array([1, 2, 3])
ypoints = np.array([5, 5, 5])

plt.subplot(2,2,2)
plt.plot(xpoints, ypoints)
plt.title("COMPANY 2")

#Plot 3
xpoints = np.array([1, 2, 3])
ypoints = np.array([4, 6, 2])

plt.subplot(2,2,3)
plt.plot(xpoints, ypoints)
plt.title("COMPANY 3")

#Plot 4
xpoints = np.array([1, 2, 3])
ypoints = np.array([2, 1, 4])

plt.subplot(2,2,4)
plt.plot(xpoints, ypoints)
plt.title("COMPANY 4")

plt.suptitle("COMPANIES DATA")
plt.show()