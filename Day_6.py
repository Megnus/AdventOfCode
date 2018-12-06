import re
from datetime import datetime
from datetime import timedelta
import operator
import numpy
import itertools

f = open('Input/input_day_6.txt', 'r')
data = f.read()
f.close()

ar1 = [[int(re.findall('\d+', s)[0]), int(re.findall('\d+', s)[1])] for s in data.splitlines()]
maxVal = [max(ar1, key=lambda x: x[0])[0], max(ar1, key=lambda x: x[1])[1]]
print(ar1.count([40, 321]))
ar2 = []
for x in range(0, 1000):
    ar2.append(min(list([[p, x, abs(p[0] - x) + abs(p[1] - 1000)] for p in ar1]), key=lambda q: q[2]))

for y in range(0, 1000):
    ar2.append(min([[p, y, abs(p[0] - 1000) + abs(p[1] - y)] for p in ar1], key=lambda q: q[2]))

ar3 = [g[0] for g in itertools.groupby(ar2, key=lambda x: x[0])]
ar4 = [ar1.index(x) for x in ar3]
print(ar3)
print(ar4)

ar5 = []
for x in range(0, 99):
    for y in range(0, 99):
        if ar1.count([x, y]) == 0:
            lista = list([[ar1.index(p), abs(p[0] - x) + abs(p[1] - y)] for p in ar1])
            minL = min(lista, key=lambda q: q[1])
            #if [x[1] for x in lista].count(minL[1]) != 1:
             #   print("NOW")
            if [x[1] for x in lista].count(minL[1]) == 1:
                ar5.append(minL[0])
print(ar5)
ar6 = [[ar1[g[0]], ar5.count(g[0])] for g in itertools.groupby(sorted(ar5), key=lambda x: x)]
print(ar6)
print([ar4.count(ar1.index(x[0])) for x in ar6])

ar7 = list(filter(lambda x: ar4.count(ar1.index(x[0])) == 0, ar6))
print(sorted(ar6, key=lambda x: x[1]))
maxx = max(ar7, key=lambda x: x[1])
print( maxx)

#>12753 12000<
exit()
# --- First star ---
i = 1
while i < len(data):
    if data[i - 1].lower() == data[i].lower() and data[i - 1] != data[i]:
        data = data.replace(data[i - 1] + data[i], '', 1)
        i -= 1 if i > 1 else 0
    else:
        i += 1

print("First star: " + str(len(data)))

# --- Second star ---
li = list(filter(lambda x: x == x.lower(), data))
ar = sorted(list(filter(lambda x: data.count(x.upper()) > 0 , li)))
groupedList = [g[0] for g in itertools.groupby(ar)]

resultMap = {}
for g in groupedList:
    replacedData = data.replace(g, '').replace(g.upper(), '')
    i = 1
    while i < len(replacedData):
        if replacedData[i - 1].lower() == replacedData[i].lower() and replacedData[i - 1] != replacedData[i]:
            replacedData = replacedData.replace(replacedData[i - 1] + replacedData[i], '', 1)
            i -= 1 if i > 1 else 0
        else:
            i += 1
    resultMap[g] = len(replacedData)

key = min(resultMap, key=resultMap.get)
print("Second star: " + str(resultMap[key]))
