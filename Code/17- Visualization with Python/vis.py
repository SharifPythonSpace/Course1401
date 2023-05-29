import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2 * np.pi, 4)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.scatter([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
ax.set_title('این یک تست است')
plt.show()
