import re
import numpy

f = open('Input/input_day_1.txt', 'r')
data = f.read().replace("\n", "")
f.close()
print(data.replace("\n", ""))
print(''.join(data.splitlines()))

x = re.split('[+|-]', data)
y = re.split('\\d+', data)
del x[0]
s = 0
arr = []
sumArr = []

for a, b in zip(x, y):
    s += int(a) if b == '+' else -int(a)
    arr.append(s)

arr = numpy.array(arr)

while True:
    sumArr.extend(arr)
    for i in sumArr:
        if sumArr.count(i) > 1:
            print("Sum: " + str(s))
            print("Twice freq: " + str(i))
            exit()
        arr = arr + s
        sumArr.extend(arr)
