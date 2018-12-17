import itertools
import re
from functools import reduce


def find(target, sub, n):
    try:
        return target.index(sub, n)
    except:
        return -1


f = open('Input/input_day_12.txt', 'r')
data = f.read()
f.close()
data = data.splitlines()
inst = data[2:]
init = re.findall('[#|.]+', data[0])[0]
inst = [re.findall('[#|.]+', x) for x in inst]
inst = [[x[0], x[1]] for x in inst]

init = 5 * '.' + init + '.' * 5
l = 0
for i in range(0, 1000):
    str_p = list(len(init) * '.')
    p = []
    for x in inst:
        n = -1
        while True:
            n = find(init, x[0], n + 1)
            if n < 0:
                break
            p.append([n + 3, x[1]])
    if len(p) > 0:
        for j in p:
            str_p[j[0]] = j[1]
        init = ''.join(str_p)
        l += (init.index('#') - 6)
        init = init.strip('.')
        init = 5 * '.' + init + '.' * 5
        count = 0
        for index in range(0, len(init)):
            if init[index] == '#':
                count += index - 5 + l
        print(i + 1, init, '  : ', l, init.rindex('#') - 5 + l, 'count :', count)

#59856 + 58 * (x - 1000)
#59856 + 58 * (50000000000 - 1000) = 2900000001856
