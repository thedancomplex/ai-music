# -*- coding: utf-8 -*-
import codecs
import pyautogui as pa
import time as t
import sys


# Website: https://codepen.io/lofaro/full/QWmRPJr

# Coordinates for X and Y when on the right screen
KeyY      =  1350
KeyX      = [2177, 2308, 2437, 2559, 2700, 2817, 2945, 3070, 3197, 3318, 3460, 3587]
TypeY     =  1407
TypeX     = [2225, 2441, 2663, 2883, 3105, 3320, 3538] 

notes     = {'C' , 'G' , 'D' , 'A' , 'E' , 'B' , 'Fs', 'Db', 'Ab', 'Eb', 'Bb', 'F' }

chromatic = {'C' , 'Db', 'D' , 'Eb', 'E' , 'F' , 'Fs', 'G' , 'Ab', 'A' , 'B' , 'Bb'} 

speed = 0.5

major = [0, 4, 7]
minor = [0, 3, 7]
dom7  = [0, 4, 7, 10]
dom   = [0, 3, 7
dim7  = [0, 3, 6, 9]
dim   = [0, 3, 6]


for x in KeyX:
  pa.moveTo(x, KeyY, speed)
  t.sleep(1.0)


#pa.moveTo(100,100,0.5)
#t.sleep(0.5)
#pa.moveTo(200,200,0.5)
#t.sleep(0.5)
