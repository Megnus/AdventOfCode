import itertools
import re
from functools import reduce



f = open('Input/input_test.txt', 'r')
data = f.read()
f.close()
data = data.splitlines()
inst = data[2:]
init = re.findall('[#|.]+', data[0])[0]
print(init)
inst = [re.findall('[#|.]+', x) for x in inst]
inst = [[x[0], '..' + x[1][0] + '..'] for x in inst]
print(inst)

for i in range(0, 20):
    for x in inst:
        l = 0
        l -= init.index('#') - 5
        init = init.strip('.')
        init = 5 * '.' + init + '.' * 5
        init = init.replace(x[0], x[1])
    print(init)



