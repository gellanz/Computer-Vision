import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import image

IMA = image.imread('bolazul.jpg')

ima = IMA.copy()[:,:,(2,2,2)] #Nivel de gris de la capa azul

filas, columnas, capas = IMA.shape[0], IMA.shape[1], IMA.shape[2]

x, y = np.arange(1,filas+1), np.arange(1,columnas+1)
fx, fy = ima[:,:,1].sum(axis = 1), ima[:,:,1].sum(axis = 0)

op1 = x * fx
op2 = y * fy

xc = (op1.sum() / fx.sum()).astype(np.uint8)
yc = (op2.sum() / fy.sum()).astype(np.uint8)

ima[xc,yc,1], ima[xc,yc,1] = 0, 0 

plt.imshow(ima)
plt.show()
