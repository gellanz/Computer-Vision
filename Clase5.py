import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import image

bul = image.imread('C1.jpg')

R = bul[:,:,[0,0,0]]
G = bul[:,:,(1,1,1)]
B = bul[:,:,(2,2,2)]
R_hist = np.zeros((256))
G_hist = np.zeros((256))
B_hist = np.zeros((256))
for i in range(bul.shape[0]):
    for j in range(bul.shape[1]):
        R_hist[R[i,j,1]] += 1
        G_hist[G[i,j,1]] += 1 
        B_hist[B[i,j,1]] += 1
plt.subplot(1,2,1)      
plt.plot(R_hist, color = 'red')
plt.plot(G_hist, color = 'green')
plt.plot(B_hist, color = 'blue')
plt.subplot(1,2,2) 
plt.imshow(bul)
plt.show()