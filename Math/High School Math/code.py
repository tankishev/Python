import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 5, 1000)
y = 2 * x + 3

ax = plt.gca()
ax.spines["bottom"].set_position('zero')
ax.spines["left"].set_position("zero")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

xticks = ax.xaxis.get_major_ticks()
yticks = ax.yaxis.get_major_ticks()
#yticks[2].set_visible(False)

plt.plot(x, y)

xloc, labels = plt.xticks()
yloc, labels = plt.yticks()
x_zero_loc = np.where(xloc==0)[0][0]
y_zero_loc = np.where(yloc==0)[0][0]

xticks[x_zero_loc].set_visible(False)
yticks[y_zero_loc].set_visible(False)

plt.show()