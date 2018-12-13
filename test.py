import itertools
import re
from functools import reduce


def func(v, n):
    global s
    for i in range(0, n):
        c = v[0]
        e = v[1]
        v = v[2:]
        v = func(v, c)
        m = v[:e]
        v = v[e:]
        s += m
    return v


def calc(v, n):
    global s
    for i in range(0, n):
        c = v[0]
        e = v[1]
        v = v[2:]
        v, s_ = calc(v, c)
        m = v[:e]
        v = v[e:]
        s += m
    return v


f = open('Input/input_day_8.txt', 'r')
data = f.read()
f.close()
ar = list(map(lambda n: int(n), data.split(' ')))
s = []

print('Raw:', ar)
func(ar, 1)
print('Sum:', sum(s))

