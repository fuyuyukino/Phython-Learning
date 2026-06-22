import matplotlib.pyplot as plt
import numpy as np

x = np.array([50, 40, 25, 35, 30, 20, 60, 45, 15, 70])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

plt.plot(x, y,"o")
plt.title("Working per Week")
plt.xlabel("Average Hours")
plt.ylabel("Number of People")
plt.grid()
plt.show()