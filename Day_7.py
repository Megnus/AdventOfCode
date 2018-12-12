import itertools
import re
from functools import reduce


def contains(array, val):
    try:
        return array.index(val) >= 0
    except ValueError:
        return False


def iterate(array, ch, old_ch):
    array = list(filter(lambda x: not contains([ch], x[0]), array))
    tmp = list(set(map(lambda x: x[1], array)))
    tmp = list(filter(lambda x: not contains(tmp, x[0]), array))
    steps = sorted(set(list(map(lambda x: x[0], tmp))))
    steps = list(filter(lambda x: not contains(old_ch, x), steps))
    time = [[x, chi(x)] for x in steps]
    return [time, array]


def chi(ch):
    return ord(ch) - 4


f = open('Input/input_day_7.txt', 'r')
data = f.read()
f.close()

array = data.splitlines()
array = [[re.findall('(?<=Step\s)[A-Z]', x)[0], re.findall('(?<=step\s)[A-Z]', x)[0]] for x in array]

ar = array
stepArray = []
while len(ar) > 0:
    temp = list(set(map(lambda x: x[1], ar)))
    temp = list(filter(lambda x: not contains(temp, x[0]), ar))
    step = sorted(set(list(map(lambda x: x[0], temp))))
    stepArray += step[0]
    temp = list(filter(lambda x: not contains(stepArray, x[0]), ar))
    ar = sorted(temp, key=lambda x: x[0])

print(''.join(stepArray))

ar = array
stepArray = []
c = ''
t = 0
old_step = []
steps = []
while len(ar) > 1:
    step, ar = iterate(ar, c, old_step)
    steps += step
    c_ar = min(steps, key=lambda x: x[1])
    c = c_ar[0]
    i = c_ar[1]
    t += c_ar[1]
    steps = list(map(lambda x: [x[0], x[1] - i], steps))
    old_step = list(map(lambda x: x[0], steps))
    c = list(filter(lambda x: x[1] == 0, steps))[0][0]
    steps = list(filter(lambda x: x[1] > 0, steps))
    stepArray += c

print(t + chi('X'))

