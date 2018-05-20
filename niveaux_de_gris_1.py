# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:47:12 2018

@author: Louise Geny
"""


from PIL import Image

img = Image.open("copie2.jpg")

copie = img.copy()


for i in range(ligne):
  for j in range(colonne):
    pixel = img.getpixel((j,i))

    gris = int(0.2125 * pixel[0] + 0.7154 * pixel[1] + 0.0721 * pixel[2])

    p = (gris,gris,gris)

    copie.putpixel((j,i), p)
    
    
copie.show()

img.close()
