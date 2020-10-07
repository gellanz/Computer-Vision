import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import image

bul = image.imread('Bulbasaur.jpg')
char = image.imread('Charmander.jpg')
squi = image.imread('Squirtle.jpg')

Charmander = [char, char[:,:,(0,0,0)], char[:,:,(1,1,1)], char[:,:,(2,2,2)]]
Bulbasaur = [bul, bul[:,:,(0,0,0)], bul[:,:,(1,1,1)], bul[:,:,(2,2,2)]]
Squirtle = [squi, squi[:,:,(0,0,0)], squi[:,:,(1,1,1)], squi[:,:,(2,2,2)]]

Pokes = Charmander + Bulbasaur + Squirtle
fig, axs = plt.subplots(3,4, figsize = (10,10))
axs = axs.ravel()

for subs, im in zip(axs,Pokes):
    subs.imshow(im)
fig.suptitle('Intensidad de color primario en cada pokemon', fontsize = 15)
plt.show()