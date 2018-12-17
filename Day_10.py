import itertools
import re
from functools import reduce
from PIL import Image
import numpy as np
import time
from graphics import *


def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


f = open('Input/input_day_10.txt', 'r')
data = f.read()
f.close()
array = data.splitlines()

print(array)
raw = [re.findall('-*\d+', x) for x in array]
raw = list(map(lambda x: [[int(x[0]), int(x[1])], [int(x[2]), int(x[3])]], raw))
#pos = list(map(lambda x: [[x[0], x[1]]], raw))
#vel = list(map(lambda x: [[x[2], x[3]]], raw))
print(max(raw, key=lambda x: x[0][0]))
print(min(raw, key=lambda x: x[0][0]))

win = GraphWin('Face', 1200, 800)  # give title and dimensions
px = 0
count = 0
while True:
    cx = raw[0][0][0]
    cy = raw[0][0][1]
    px = 0
    py = 0
    dr = 0
    for e in raw:
        x = cx + e[0][0]
        y = cy + e[0][1]
        dr += px + x
        vx = e[1][0]
        vy = e[1][1]
        if count == 10240:
            pt = Point(x, y)
            pt.draw(win)
            print(count * 3)
        px = x
        py = y
        e[0][0] += vx
        e[0][1] += vy
    #for i in raw:
        #print(i)
        """if count > 10228:
        time.sleep(1)
        clear(win)"""
    count += 1
    #print(dr, count)
    # RLEZNRAN



pt = Point(400, 50)
pt.draw(win)
win.getMouse()
win.close()

