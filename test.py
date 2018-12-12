import itertools
import re
from functools import reduce


def contains(array, val):
    try:
        return array.index(val) >= 0
    except ValueError:
        return False

# GKPTSLUXBIJMNCADFOVHEWYQRZ
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
print(''.join(stepArray) == 'GKPTSLUXBIJMNCADFOVHEWYQRZ')
exit()

# Get right elements from basic list
temp = list(set(map(lambda x: x[1], ar)))

# Get all left element that is not in right element.
temp = list(filter(lambda x: not contains(temp, x[0]), ar))

# Get all al left elements that is unique sorted.
step = sorted(set(list(map(lambda x: x[0], temp))))

stepArray += step[0]

print(stepArray)

temp = list(filter(lambda x: not contains(stepArray, x[0]), ar))
ar = sorted(temp, key=lambda x: x[0])
print(ar)

# Get right elements from basic list
temp = list(set(map(lambda x: x[1], ar)))

# Get all left element that is not in right element.
temp = list(filter(lambda x: not contains(temp, x[0]), ar))

# Get all al left elements that is unique sorted.
step = sorted(set(list(map(lambda x: x[0], temp))))

stepArray += step[0]
print(stepArray)

#-----------------------

temp = list(filter(lambda x: not contains(stepArray, x[0]), ar))
ar = sorted(temp, key=lambda x: x[0])
print(ar)

# Get right elements from basic list
temp = list(set(map(lambda x: x[1], ar)))

# Get all left element that is not in right element.
temp = list(filter(lambda x: not contains(temp, x[0]), ar))

# Get all al left elements that is unique sorted.
step = sorted(set(list(map(lambda x: x[0], temp))))
print(step)
stepArray += step[0]
print(stepArray)

#-----------------------

temp = list(filter(lambda x: not contains(stepArray, x[0]), ar))
ar = sorted(temp, key=lambda x: x[0])
print(ar)

# Get right elements from basic list
temp = list(set(map(lambda x: x[1], ar)))

# Get all left element that is not in right element.
temp = list(filter(lambda x: not contains(temp, x[0]), ar))

# Get all al left elements that is unique sorted.
step = sorted(set(list(map(lambda x: x[0], temp))))
print(step)
stepArray += step[0]
print(stepArray)

#-----------------------

temp = list(filter(lambda x: not contains(stepArray, x[0]), ar))
ar = sorted(temp, key=lambda x: x[0])
print(ar)

# Get right elements from basic list
temp = list(set(map(lambda x: x[1], ar)))

# Get all left element that is not in right element.
temp = list(filter(lambda x: not contains(temp, x[0]), ar))

# Get all al left elements that is unique sorted.
step = sorted(set(list(map(lambda x: x[0], temp))))
print(step)
stepArray += step[0]
print(stepArray)












exit()
temp1 = list(set(map(lambda x: x[1], ar1)))

# Get all left element that is not in right element.
temp1 = list(filter(lambda x: not contains(temp1, x[0]), ar1))

# Get all al left elements that is unique sorted.
step2 = sorted(set(list(map(lambda x: x[0], temp1))))

print(step2)
print(temp1)


#temp = sorted(list(set(map(lambda x: x[1], temp))))
#temp = sorted(temp, key=lambda x: x[0])

#print(temp)
