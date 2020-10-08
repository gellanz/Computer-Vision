import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import image

bul = image.imread('Bulbasaur.jpg') 

bul =  (0.2989 * bul[:,:,(0,0,0)] + 0.587 * bul[:,:,(1,1,1)] + 0.114 * bul[:,:,(2,2,2)]).astype(np.uint8)
# Umbral a cierto nivel n, se ven contornos
# n = 150
# (bul>n).astype(int)*255
plt.imshow()
plt.show()