import re
from datetime import datetime
from datetime import timedelta
import operator
import numpy
import itertools

f = open('Input/input_day_5.txt', 'r')
data = f.read()
f.close()

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
