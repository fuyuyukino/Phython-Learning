import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10,20,30,40,50])
mylabels = ["Apple", "Orange", "Banana", "Grape", "Melon"]
myexplode = [0, 0, 0, 0.2, 0]

plt.pie(xpoints, labels = mylabels, startangle = 180, explode = myexplode)
plt.legend(title = "Fruits")
plt.show()