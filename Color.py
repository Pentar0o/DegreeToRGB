#-*- coding: utf-8 -*-
from math import *
import numpy as np
import cv2

#On créé une image noir de 1024x512
img = np.zeros(shape=[200,1920,4], dtype = np.uint8)

Temp = 0
x = 15
y = 40

for Temp in range(37):
    Angle = Temp*5
    #On converti l'angle de degrée en radians
    AngleRad = radians(Angle)

    R = int(-cos(AngleRad)*255)
    G = int(sin(AngleRad)*255)
    B = int(cos(AngleRad)*255)

    if R < 0 : R = 0
    if G < 0 : G = 0
    if B < 0 : B = 0


    #print("Temp : " + str(Temp) + " R:" + str(R) + " G:" + str(G) + " B:" + str(B))

    #On dessine les rectangles
    cv2.putText(img, str(Temp), (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(R,G,B), 1)
    cv2.rectangle(img, (x, y+20), (x+40, y+40), (R, G, B), -1)

    x = x + 50

#On convertit l'image de BGR en RGB
RGBimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite('/mnt/c/Users/penta/Desktop/test.jpg',RGBimg)

