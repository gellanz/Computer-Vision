import numpy as np
import matplotlib.pyplot as plt 

x, y = 255, 255

cara1 = np.zeros([x,y,3], dtype = np.uint8)
cara2 = np.zeros([x,y,3], dtype = np.uint8)
cara3 = np.zeros([x,y,3], dtype = np.uint8)
cara4 = np.zeros([x,y,3], dtype = np.uint8)
cara5 = np.zeros([x,y,3], dtype = np.uint8)
cara6 = np.zeros([x,y,3], dtype = np.uint8)

for i in range(x):
    for j in range(y):

        cara1[i,j,0] = j #R
        cara1[i,j,1] = i #G
        cara1[i,j,2] = 0 #B

        cara2[i,j,0] = j #R
        cara2[i,j,1] = 0 #G
        cara2[i,j,2] = 255-i #B

        cara3[i,j,0] = 0 #R
        cara3[i,j,1] = i #G
        cara3[i,j,2] = 255-j #B

        cara4[i,j,0] = 255 #R
        cara4[i,j,1] = i #G
        cara4[i,j,2] = j #B

        cara5[i,j,0] = j #R
        cara5[i,j,1] = 255 #G
        cara5[i,j,2] = i #B

        cara6[i,j,0] = 255-j #R
        cara6[i,j,1] = i #G
        cara6[i,j,2] = 255 #B

plt.subplot(3,4,6)
plt.imshow(cara1)

plt.subplot(3,4,2)
plt.imshow(cara2)

plt.subplot(3,4,5)
plt.imshow(cara3)

plt.subplot(3,4,7)
plt.imshow(cara4)

plt.subplot(3,4,10)
plt.imshow(cara5)

plt.subplot(3,4,8)
plt.imshow(cara6)

plt.show()