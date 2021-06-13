import itertools
import re
from functools import reduce

f = open('Input/input_test.txt', 'r')
data = f.read()
f.close()
array = data.splitlines()
print(array)
print(list(map(lambda x: re.findall('\d+', x), array)))

p = 0
n = 0
ar = [0]
player = 1
point = {}
num_player = 424
counter = 0;

for i in range(1, num_player + 1):
    point[i] = 0

while n < 71144*100:
    if n % 71144 == 0:
        counter += 1
        print(counter, '%')

    n += 1
    if n % 23 == 0:
        p -= 7
        if p < 0:
            p += len(ar)
        point[player] += n + ar[p]
        ar.pop(p)
    else:
        p += 2
        if p > len(ar):
            p -= len(ar)
        ar.insert(p, n)

    if player % num_player == 0:
        player = 0

    player += 1


print(max(point.values()))
