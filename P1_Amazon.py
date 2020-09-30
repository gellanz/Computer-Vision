import numpy as np
import matplotlib.pyplot as plt 

x, y = 500, 600
f = np.zeros((x,y,3))
for i in range(x):
    for j in range(y):
        exp1 = np.power(i-100,2) + np.power(j-255, 2) 
        exp2 = np.power(i-20,2) + np.power(j-265, 2)
        # if (67 > i > 420) and (177 > j > 218):
        if (41500 > exp1 > 40500) and (70 < j < 420):
            f[i][j] = 255
        if (65000 > exp2 > 64000) and (70 < j < 420) :
            f[i][j] = 255

plt.imshow(f)
plt.show()

# and (67 > j > 420) and (177 > i > 218)
# and (67 > j > 420) and (177 > i > 218)