from __future__ import division
import pygame, sys
from pygame.locals import *
from random import *
from types import *
pygame.init()

""" binaryEvaluator.py
by Eric J.Parfitt (ejparfitt@gmail.com)

This program turns a binary sequence into a series of left and right
turns, in order to visualize the sequence.  If two lines collide, the
visualizer jumps to the right and begins drawing a new curve. 

Version: 1.0 alpha
"""

def draw():
    windowSurface.fill(WHITE)
    pygame.display.flip()

def update():
    clock.tick(FPS)

def inc(direction):
    if (direction + 1) < DIRECTION_NUM:
        return direction + 1
    return 0

def dec(direction):
    if (direction) >= 1:
        return direction -1
    return DIRECTION_NUM - 1

def toList(binary):
    binaryList =[]
    for binaryNum in binary:
        binaryList.append(int(binaryNum))
    return binaryList

def checkQuit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

WIDTH = 1800
HEIGHT = 600

DIRECTION_NUM = 4
LINE_LENGTH = 20
OFFSET = 200

randBinList = lambda n: [randint(0,1) for b in range(1,n+1)]

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 5
clock = pygame.time.Clock()

#binaryNums = randBinList(150)
#123 digits of pi
binaryNums = toList("11001001000011111101101010100010001000010110100011000010\
001101001100010011000110011000101000101110000000110111000")
print(binaryNums)
binaryNums = [0] + binaryNums
windowSurface.fill(WHITE)
position = [100, int(round(HEIGHT / 2))]
oldPosition = [None, None]
direction = 0
oldPositions = []
isOverlap = False
midPoint = None
midPoints = []
for binaryNum in binaryNums:
    isPositionEq = isOldPositionEq = False
    oldPosition[0] = position[0]
    oldPosition[1] = position[1]
    if binaryNum == 0:
        direction = inc(direction)
    else:
        direction = dec(direction)
    if direction == 0:
        position[0] += LINE_LENGTH
    elif direction == 1:
        position[1] -= LINE_LENGTH
    elif direction == 2:
        position[0] -= LINE_LENGTH
    elif direction == 3:
        position[1] += LINE_LENGTH
    if not oldPosition[0] == None:
        midPoint = ((oldPosition[0] + position[0]) / 2,
                (oldPosition[1] + position[1]) / 2)
        for oldMidPoint in midPoints:
            if oldMidPoint[0] == midPoint[0] and oldMidPoint[1] == midPoint[1]:
                oldPosition[0] += OFFSET
                oldPosition[1] = oldPosition[1]
                position[0] += OFFSET
                position[1] = position[1]
        midPoint = ((oldPosition[0] + position[0]) / 2,
                (oldPosition[1] + position[1]) / 2)
        midPoints.append(midPoint)
    checkQuit()
    pygame.draw.line(windowSurface, BLACK, oldPosition, position)
    pygame.draw.circle(windowSurface, BLACK, position, 2)
    pygame.draw.circle(windowSurface, WHITE, oldPosition, 2)
    pygame.display.flip()
    clock.tick(FPS)
while True:
    checkQuit()
    clock.tick(60)
