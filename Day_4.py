import re
from datetime import datetime
from datetime import timedelta
import operator
import numpy

f = open('Input/input_day_4.txt', 'r')
data = f.read()
f.close()

datetime_object = datetime.strptime('1518-10-17 00:13', '%Y-%m-%d %H:%M')

ar1 = [[re.search('\d{3}.+\d{2}:\d{2}', x).group(0), re.search('(?<=\]\s).+', x).group(0)]  for x in data.splitlines()]
ar2 = sorted(ar1, key=lambda x: x[0])
ar3 = [[datetime.strptime(x[0], '%Y-%m-%d %H:%M'), x[1]] for x in ar2]

ar3x = sorted(ar3, key=lambda x: x[0])
for x in ar3x:
    print(x[0].strftime("%Y-%m-%d %H:%M:%S"), x[1])

ar4 = []
for x in ar3:
    if re.match('Guard #\d+ begins shift', x[1]) is not None:
        gard = re.search('\d+', x[1]).group(0)
        t1 = x[0]
    elif re.match('wakes up', x[1]) is not None:
        t2 = x[0].hour
        ar4.append([gard, int(t1.strftime("%M")), int(x[0].strftime("%M")), int(x[0].strftime("%M")) - int(t1.strftime("%M"))])
    elif re.match('falls asleep', x[1]) is not None:
        t1 = x[0]

ara = sorted(ar4, key=lambda x: x[0])
[print(x) for x in ara]

map1 = {}
for x in ara:
    map1[x[0]] = 0

for x in ara:
    map1[x[0]] += x[3]

for x in map1:
    print(x, map1[x])

print(max(map1.values()))

maxdate = datetime.strptime('01:00', '%H:%M').time()
d = timedelta(minutes=0)
maxd = timedelta(minutes=60)

map1 = {}
for x in ara:
    map1[x[0]] = [numpy.full(60, 0), numpy.full(60, 0), numpy.full(60, 0)]

for x in ara:
    c = ' '
    for i in range(0, 59):
        if i == x[1]:
            c = 'x'
        if i == x[2]:
            c = ' '
        if c == 'x':
            map1[x[0]][1][i] += 1

        map1[x[0]][0][i] += 1

        print(c, end='')
    print(x[0], end=' ')
    print()

for i in range(0, 59):
    print(str(i).zfill(2), end=' ')

print(1777)
for x in map1:
    c = ' '
    for i in range(0, 59):
        map1[x][2][i] = map1[x][1][i]*100 / map1[x][0][i]
    #for j in map1[x][2]:
    #    print(str(j).zfill(2), end=' ')
    for j in map1[x][1]:
        print(str(j).zfill(2), end=' ')

    print(str(x).zfill(4), end=' ')
    #print(str(map1[x][1].max()).zfill(2), end=' ')
    print(str(map1[x][1].max()).zfill(2), end=' ')
    print(list(map1[x][2]).index(map1[x][2].max()), end=' ')
    print()

print(2903*40, 2903*41, 2903*38)
exit()

ar5 = list(filter(lambda x: x[4] is not None, ar4))
ar6 = sorted(ar5, key=lambda x: x[2])
ar7 = list(numpy.full(10, 0)) + list(numpy.full(5, 1)) + list(numpy.full(4, 0))
print(ar6)

map1 = {}
for x in ar6:
    map1[x[0]] = numpy.full(60, 0)

for x in ar6:
    map1[x[0]] = numpy.add(map1[x[0]], x[4])

for x in map1:
    print(x, max(map1[x]))


print(map1['1889'], list(map1['1889']).index(16) + 1, 1889 * 32)
exit()
t = timedelta(microseconds=0)


"""
ar7 = {}
guard = "";
for x in ar6:
    if x[0] != guard:
        ar7[x[0]] = timedelta(microseconds=0)
    if t.total_seconds() == 0 and x[1] == 'f':
        t = x[3]
    if t == timedelta(microseconds=0) and x[1] == 'f':
"""
ar7 = {}
for x in ar6:
    ar7[x[0]] = timedelta(microseconds=0)

for x in ar6:
    ar7[x[0]] += x[3]
print("------------------")
for x in ar7:
    print(x, ar7[x])

key_ = max(ar7.items(), key=operator.itemgetter(1))[0]
val_ = int(ar7[key_].total_seconds() / 60)

print(key_, val_, int(key_) * val_)
