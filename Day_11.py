def power(x, y, sn):
    res = ((x + 10) * y + sn) * (x + 10)
    res = ((res - (res % 100)) % 1000) / 100 - 5
    return int(res)

sn = 5719
#print(power(101, 153, 5719))
path = [[0 for x in range(300)] for y in range(300)]
for x in range(0, 300):
    for y in range(0, 300):
        path[x][y] = power(x, y, sn)

powerM = [[[0 for k in range(300)] for x in range(300)] for y in range(300)]

for x in range(0, 300):
    for y in range(0, 300):
        print(x, y)
        for k in range(0, 300):
            if k + x > 300 or k + y > 300:
                break
            area = 0
            for i in range(0, k):
                for j in range(0, k):
                    area += path[x + i][y + j]
            powerM[x][y][k] += area

#m = max(map(max, powerM))
m = -1000
for x in range(0, 300):
    for y in range(0, 300):
        for k in range(0, 300):
            if powerM[x][y][k] > m:
                m = powerM[x][y][k]
                print(x, y, k)

