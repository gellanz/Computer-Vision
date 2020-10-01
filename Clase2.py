import numpy as np
import matplotlib.pyplot as plt 

x, y = 255, 255
f = np.zeros([x,y,3], dtype = np.uint8)

for i in range(x):
    for j in range(y):
        # print(i,j)
        f[i,j,0] = 255-i #R
        f[i,j,1] = j #G
        f[i,j,2] = 0 #B

# plt.imshow(np.fliplr(f))
plt.imshow(f)
plt.show()