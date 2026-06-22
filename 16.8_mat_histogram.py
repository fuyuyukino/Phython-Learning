import matplotlib.pyplot as plt
import numpy as np

xpoints = np.random.normal(100, 25, 2500)

plt.hist(xpoints)
plt.show()