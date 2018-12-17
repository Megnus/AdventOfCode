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
    s = []
    for i in range(0, n):
        c = v[0]
        e = v[1]
        v = v[2:]
        v, t = calc(v, c)
        m = v[:e]
        if c != 0:
            m = list(map(lambda x: t[x - 1] if x <= len(t) else 0, m))
        s.append(sum(m))
        v = v[e:]

    return v, s


su_=[1, 2, 3, 7, 5]
m = [1, 1, 5, 4, 3, 10]


f = open('Input/input_test.txt', 'r')
f = open('Input/input_day_8.txt', 'r')
data = f.read()
f.close()
ar = list(map(lambda n: int(n), data.split(' ')))
s = []

print('Raw:', ar)
func(ar, 1)
print('First star:', sum(s))
print('Second star:', calc(ar, 1)[1][0])

