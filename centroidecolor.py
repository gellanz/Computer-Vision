import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import image

IMA = image.imread('bolazul.jpg')

ima = IMA[:,:,(2,2,2)]#Nivel de gris de la capa azul

filas, columnas, capas = IMA.shape[0], IMA.shape[1], IMA.shape[2]

x, y = np.arange(1,filas+1), np.arange(1,columnas+1)
fx, fy = ima[:,:,1].sum(axis = 1), ima[:,:,1].sum(axis = 0)

op1 = x * fx
op2 = y * fy

xc = (op1.sum() / fx.sum()).astype(np.uint8)
yc = (op2.sum() / fy.sum()).astype(np.uint8)

ima[xc,yc,1], ima[xc,yc,0] = 0, 0 

plt.subplot(1,2,1)
plt.imshow(ima)
plt.subplot(1,2,2)
plt.imshow(IMA)
plt.show()
