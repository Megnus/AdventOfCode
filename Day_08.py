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
    su = []
    for i in range(0, n):
        c = v[0]
        e = v[1]
        v = v[2:]
        v, su_ = calc(v, c)
        m = v[:e]
        v = v[e:]
        print('New shit:',  su_, m)
        su += m + su_
    return v, su


f = open('Input/input_test.txt', 'r')
data = f.read()
ar = list(map(lambda n: int(n), data.split(' ')))
f.close()
s = []
print('Raw:', ar)
print(calc(ar, 1))
print('Sum:', sum(s))
