#Elizarraras Llanos Angel Gustavo
import numpy as np
import matplotlib.pyplot as plt 

x, y = 500, 600
f = np.zeros((x,y,3))
a, b = np.sin(-0.6), np.cos(-0.6)

for i in range(x):
    for j in range(y):
        #Circulos de la sonrisa
        #Smile circles
        circulo1 = (i-100) ** 2 + (j-255) ** 2
        circulo2 = (i-20) ** 2 + (j-265) ** 2

        #Boomerang hecho a base de elipses
        #Boomerang made with elipses
        elipse1 = ((i*b - j*a - 420)**2 / 4) + ((i*a + j*b -135)**2 / 20)        
        elipse2 = ((i*b - j*a - 420)**2 / 3) + ((i*a + j*b -150)**2 / 20)
        
        #Perimetros de las figuras con un rango y con limites
        if (41500 > circulo1 > 40500) and (70 < j < 420):
            f[i][j] = 255
        elif (65000 > circulo2 > 64000) and (70 < j < 420) :
            f[i][j] = 255
        elif (450 < elipse1 < 500) and ( 392 < j < 450 ) and (i < 260):
            f[i][j] = 255
        elif (450 < elipse2 < 500) and ( 392 < j < 450 )and (i < 260):
            f[i][j] = 255

plt.imshow(f)
plt.title('P1 - Amazon Logo - Elizarraras')
plt.show()
