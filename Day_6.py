import re
from datetime import datetime
from datetime import timedelta
import operator
# import numpy
import itertools

f = open('Input/input_day_6.txt', 'r')
data = f.read()
f.close()

ar1 = [[int(re.findall('\d+', s)[0]), int(re.findall('\d+', s)[1])] for s in data.splitlines()]
maxVal = [max(ar1, key=lambda x: x[0])[0], max(ar1, key=lambda x: x[1])[1]]


def dist(a, b, ar):
    return sum([abs(a - p[0]) + abs(b - p[1]) for p in ar]) < 10000


M = []
for x in range(-1000, 1000):
    print(100 * (x + 1000) / 2000)
    for y in range(-1000, 1000):
        if dist(x, y, ar1):
            M.append([x, y])
print(len(M))
exit()


def func1(p, x_, y_):
    return abs(p[0] - x_) + abs(p[1] - y_)


def func(p, x_, y_):
    return abs(p[0] - x_) if abs(p[0] - x_) > abs(p[1] - y_) else abs(p[1] - y_)


print(ar1.count([40, 321]))
ar2 = []
for x in range(-1000, 1000):
    ar2.append(min(list([[p, x, func1(p, x, 1000)] for p in ar1]), key=lambda q: q[2]))

for x in range(-1000, 1000):
    ar2.append(min(list([[p, x, func1(p, x, -1000)] for p in ar1]), key=lambda q: q[2]))

for y in range(-1000, 1000):
    ar2.append(min([[p, y, func1(p, 1000, y)] for p in ar1], key=lambda q: q[2]))

for y in range(-1000, 1000):
    ar2.append(min([[p, y, func1(p, -1000, y)] for p in ar1], key=lambda q: q[2]))

ar3 = [g[0] for g in itertools.groupby(ar2, key=lambda x: x[0])]
ar4 = [ar1.index(x) for x in ar3]
print(ar3)
print(ar4)

ar5 = []
for x in range(-500, 500):
    print(100 * (x + 500) / 1000)
    for y in range(-500, 500):
        li = list([[ar1.index(p), func1(p, x, y)] for p in ar1])
        minL = min(li, key=lambda q: q[1])
        if [x[1] for x in li].count(minL[1]) == 1:
            ar5.append(minL[0])
print(ar5)
ar6 = [[ar1[g[0]], ar5.count(g[0])] for g in itertools.groupby(sorted(ar5), key=lambda x: x)]
print(ar6)
print([ar4.count(ar1.index(x[0])) for x in ar6])

ar7 = list(filter(lambda x: ar4.count(ar1.index(x[0])) == 0, ar6))
print(sorted(ar6, key=lambda x: x[1]))
maxx = max(ar7, key=lambda x: x[1])
print(maxx)
