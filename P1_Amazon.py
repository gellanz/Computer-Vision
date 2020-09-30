import numpy as np
import matplotlib.pyplot as plt 

x, y = 500, 600
f = np.zeros((x,y,3))
a, b = np.sin(-0.6), np.cos(-0.6)

for i in range(x):
    for j in range(y):
        #Circulos de la sonrisa
        #Smile circles
        exp1 = (i-100) ** 2 + (j-255) ** 2
        exp2 = (i-20) ** 2 + (j-265) ** 2

        #Boomerang hecho a base de elipses
        #Boomerang made with elipses
        exp3 = ((i*b - j*a - 420)**2 / 4) + ((i*a + j*b -135)**2 / 20)        
        exp4 = ((i*b - j*a - 420)**2 / 3) + ((i*a + j*b -150)**2 / 20)

        if (41500 > exp1 > 40500) and (70 < j < 420):
            f[i][j] = 255
        elif (65000 > exp2 > 64000) and (70 < j < 420) :
            f[i][j] = 255
        elif (450 < exp3 < 500) and ( 392 < j < 450 ) and (i < 260):
            f[i][j] = 255
        elif (450 < exp4 < 500) and ( 392 < j < 450 )and (i < 260):
            f[i][j] = 255

plt.imshow(f)
plt.show()
