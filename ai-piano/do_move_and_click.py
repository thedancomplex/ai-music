# -*- coding: utf-8 -*-
import codecs
import pyautogui as pa
import time as t
import sys
import random

# Website: https://codepen.io/lofaro/full/QWmRPJr

# Coordinates for X and Y when on the right screen

class AiPiano:
  KeyY      =  1350
  KeyX      = [2177, 2308, 2437, 2559, 2700, 2817, 2945, 3070, 3197, 3318, 3460, 3587]
  TypeY     =  1407
  TypeX     = [2225, 2441, 2663, 2883, 3105, 3320, 3538] 

  notes     = ['C' , 'G' , 'D' , 'A' , 'E' , 'B' , 'Fs', 'Db', 'Ab', 'Eb', 'Bb', 'F' ]

  chromatic = ['C' , 'Db', 'D' , 'Eb', 'E' , 'F' , 'Fs', 'G' , 'Ab', 'A' , 'B' , 'Bb']

  types     = ['Ionlan', 'Dorian', 'Phryglan', 'Lydlan', 'Mixolydlan', 'Aeollan', 'Locrian']

  scaleType = ['major', 'minor', 'dom7', 'dom', 'dim7', 'dim']

  speed = 0.5

  major = [0, 4, 7]
  minor = [0, 3, 7]
  dom7  = [0, 4, 7, 10]
  dom   = [0, 3, 7]
  dim7  = [0, 3, 6, 9 ]
  dim   = [0, 3, 6]

  def __init__(self):
    pass

  def getScaleTypeRand(self):
    ri = random.randint(0,len(self.scaleType)-1)
    return self.scaleType[ri]
    
  def getTypeRand(self):
    ri = random.randint(0,len(self.types)-1)
    return self.types[ri]
    
  def getKeyRand(self):
    ri = random.randint(0,len(self.chromatic)-1)
    return self.chromatic[ri]

  def setKey(self,theKey=None):
    if theKey == None:
      return 1
    print('Key = ', end='')
    print(theKey)
    x = self.notes.index(theKey)
    pa.moveTo(self.KeyX[x], self.KeyY, self.speed)
    t.sleep(3.0)
    pa.click()
    t.sleep(0.5)
    return 0
  

  def setType(self,theType=None):
    if theType == None:
      return 1
    print('Type = ',end='')
    print(theType)
    x = self.types.index(theType)
    pa.moveTo(self.TypeX[x], self.TypeY, self.speed)
    t.sleep(3.0)
    pa.click()
    t.sleep(0.5)
    return 0
  
  def getProgression(self, theType='major', theKey='C', theLen=5):
    if theType == None:
      return None

    scale = []
    if theType == 'major':
      scale = self.major
    elif theType == 'minor':
      scale = self.minor
    elif ( (theType == 'dim7') | (theType == 'diminished7') ):
      scale = self.dim7
    elif ( (theType == 'dom7') | (theType == 'dominant7') ):
      scale = self.dom7
    elif ( (theType == 'dim') | (theType == 'diminished') ):
      scale = self.dim
    elif ( (theType == 'dom') | (theType == 'dominant') ):
      scale = self.dom
    else:
      return None

    theOut = []

    theShift = self.chromatic.index(theKey)

    for i in range(theLen):
      for x in scale:
        theOut.append(x)
    theOut.append(scale[0])


    # apply shift
    theOut = [x+theShift for x in theOut]

    numOut = []
    for x in theOut:
      if x >= len(self.chromatic):
        x = x - len(self.chromatic)
      numOut.append(x)

    strOut = []

    for x in numOut:
      strOut.append(self.chromatic[x])

    return strOut

  def getLen(self):
    ri = random.randint(0,7)
    ri += 3
    return ri
    

  def getSongBase(self):
    theLen       = self.getLen()
    theType      = self.getTypeRand()
    theScaleType = self.getScaleTypeRand()
    theKey       = self.getKeyRand()
    progression  = self.getProgression(theType=theScaleType, theKey=theKey, theLen=theLen)

    print(theType, end=' - ')
    print(theKey, end=' ')
    print(theScaleType)
    print(progression)
    return (theType, theScaleType, theKey, progression)

  def getTime(self):
    dt = random.randint(10,60)
    dt = dt*1.00001
    return dt

def main():
  mus = AiPiano()

  while True:
    theType, theScaleType, theKey, progression = mus.getSongBase()
    print(theType, end=' - ')
    print(theKey, end=' ')
    print(theScaleType)
    print(progression)
    
    dt = mus.getTime()
    print('Time per segment = ', end='')
    print(dt)

    ## Set the type

    # Random - AIPIANO1
    #mus.setType(theType)

    # Set to Ionlan - AIPIANO2
    #mus.setType('Ionlan')

    # Set to Ionlan - AIPIANO3
    mus.setType('Dorian')

    for val in progression:
      mus.setKey(val)
      t.sleep(dt)


#
#  for x in mus.chromatic:
#    mus.setKey(x)
#    t.sleep(1.0)  
#  for x in mus.types:
#    mus.setType(x)
#    t.sleep(1.0)  

main()



#  pa.moveTo(x, KeyY, speed)
#  t.sleep(3.0)
#  pa.click()
#  t.speel(0.5)


#pa.moveTo(100,100,0.5)
#t.sleep(0.5)
#pa.moveTo(200,200,0.5)
#t.sleep(0.5)
