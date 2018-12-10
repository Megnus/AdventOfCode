import re

from datetime import datetime
from datetime import timedelta
import operator
import numpy
import itertools


def swap(arr, swpr):
    x = swpr[0]
    y = swpr[1]
    arr[arr.index(x)], arr[arr.index(y)] = arr[arr.index(y)], arr[arr.index(x)]


def sort_by(myset, ar2):
    eq = True
    while eq:
        new_set = myset.copy()
        for e in ar2:
            swap(myset, e)
            eq = False
        for q, w in zip(new_set, myset):
            if q != w:
                eq = True
                break


def sort_by_b(a_set, b_set):
    eq = True
    tt = 0
    while eq:
        tt += 1
        new_set = a_set.copy()
        for i in range(1, len(a_set)):
            a = a_set[i - 1]
            b = a_set[i]
            if a > b:
                eqq = False
                for x in b_set:
                    if x == [a, b]:
                        eqq = True
                        break
                if not eqq:
                    a_set[i - 1] = b
                    a_set[i] = a
        #print(a_set)
        eq = False
        for q, w in zip(new_set, myset):
            if q != w:
                eq = True
                break

f = open('Input/input_day_7.txt', 'r')
data = f.read()
f.close()

ar1 = data.splitlines()
ar2 = [[re.findall('(?<=Step\s)[A-Z]', x)[0], re.findall('(?<=step\s)[A-Z]', x)[0]] for x in ar1]

#flatten
flat_list = [item for sublist in ar2 for item in sublist]

#uniqe
ar3 = list(set(flat_list))
print(ar3)

for x in ar2:
    te = True
    for y in ar2:
        if x[0] == y[1]:
            te = False
            break
    if te:
        print(x)

n = 0
print(ar3)
while n < 10:
    for x in ar2:
        i = ar3.index(x[0])
        j = ar3.index(x[1])
        if i > j:
            #print(x[0], i, x[1], j)
            ar3[i], ar3[j] = ar3[j], ar3[i]
            #ar3[j + 1], ar3[j] = ar3[j], ar3[j + 1]
            #i = ar3.index(x[0])
            #j = ar3.index(x[1])
            #print(x[0], i, x[1], j)
            #break
    print(ar3)
    n += 1
print("----------------")















exit()
#print(list(filter(lambda x: x[0] == 'N' or x[1] == 'N', ar2)))
#myset = sorted(myset)

print(myset)


sort_by(myset, ar2)

print(myset)
exit()
#sort_by_b(myset, ar2)

print(myset)

for k in range(0, 100000):
    sort_by(myset, ar2)

print(''.join(myset) == 'CFGHAEMNBPRDIVWQSUZJYTKLOX')
print(''.join(myset))
#CFGHAEMNBRDPIVWQSUZJYTKLOX
#CFGHAEMNBPRDIVWQSUZJYTKLOX
#CFGHAEMNBPRDIWQUZJVYTKLOSX
#FGHAEMNBCPRDIWQUZJSVYTKLOX
#FGHAEMNBCPRDIVWQUZJYTKLOSX
#CFGHAEMNBPRDIVWQUZJSYTKLOX
#CFGHAEMNBPRDIVWQSUZJYTKLOX

#FGHAMNBCEPRDIVWQSUZJYTKLOX
#FGHACEMNBPRDIWQUVZJSYTKLOX
#CFGHAEMNBRDPISWQUZJYTKVLOX
#CFGHAEMNBPRDISVWQUZJYTKLOX
#CFGHAEMNBPRDIVWQUZJYTKLOSX
#CFGHAEMNBPRDIVWQUZJYTKLOSX

exit()
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
