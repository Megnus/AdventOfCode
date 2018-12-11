import itertools
import re
from functools import reduce


def contains(array, val):
    try:
        return array.index(val) >= 0
    except ValueError:
        return False

# GKPTSLUXBIJMNCADFOVHEWYQRZ
# 920


f = open('Input/input_day_7.txt', 'r')
data = f.read()
f.close()

ar = data.splitlines()
ar = [[re.findall('(?<=Step\s)[A-Z]', x)[0], re.findall('(?<=step\s)[A-Z]', x)[0]] for x in ar]

stepArray = []

while len(ar) > 0:
      temp = list(set(map(lambda x: x[1], ar)))
      temp = list(filter(lambda x: not contains(temp, x[0]), ar))
      step = sorted(set(list(map(lambda x: x[0], temp))))
      stepArray += step[0]
      print(stepArray)
      temp = list(filter(lambda x: not contains(stepArray, x[0]), ar))
      ar = sorted(temp, key=lambda x: x[0])
      print(ar)

print(''.join(stepArray))
exit()