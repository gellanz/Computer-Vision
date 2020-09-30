import numpy as np
import matplotlib.pyplot as plt 

x, y = 600, 600
f = np.empty((600,600,3))

for i in range(x):
    for j in range(y):

        if (np.power((i - x/2), 2) + np.power((j - y/2), 2)) < 100000:
            f[i][j] = 255
        else:
            f[i][j] = 0

        # if i == x/2:
        #     f[i][j] = 255
        # elif j == y/2:
        #     f[i][j] = 255
        # else:
        #     f[i][j] = 0

        # f[i][j] = (127 * np.sin(0.1 * i) + 127 * np.sin(0.1 * j) / 2) + 127


plt.imshow(f)
plt.show()
