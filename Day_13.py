import itertools
import re
from functools import reduce


def is_in(v, e):
    try:
        v.index(e)
        return True
    except ValueError:
        return False

def find(vec, elm):
    vec = list(map(lambda x: x[0], vec))
    try:
        return vec.index(elm)
    except ValueError:
        return -1


def get(vec, elm):
    idx = find(vec, elm)
    if idx >= 0:
        return vec[idx][1]


#car = [[x, y], [v, n]]
def new_pos(car):
    M = {'v': [0, 1], '<': [-1, 0], '>': [1, 0], '^': [0, -1]}
    car[0][0] += M[car[1][0]][0]
    car[0][1] += M[car[1][0]][1]
    return car


def new_vel(car, track_p):
    M = {'\\': {'v': '>', '<': '^', '>': 'v', '^': '<'},
         '/': {'v': '<', '<': 'v', '>': '^', '^': '>'}}
    S = ['>', '^', '<', 'v']
    N = [1, 0, -1]

    if track_p == '+':
        xx = car[1][0]
        ro = N[car[1][1]]
        index = S.index(car[1][0]) + N[car[1][1]]
        index = 3 if index < 0 else index % 4
        car[1][0] = S[index]
        car[1][1] = (car[1][1] + 1) % 3
        #print(xx, car[1][0], ro)
    else:
      car[1][0] = M[track_p][car[1][0]]

    return car


f = open('Input/input_test.txt', 'r')
f = open('Input/input_day_13_test.txt', 'r')
f = open('Input/input_day_13.txt', 'r')
data = f.read()
f.close()
data = data.splitlines()

v = []
cars = []
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        c = data[y][x]
        if c == '\\' or c == '/' or c == '+':
            v.append([[x, y], c])
        elif c == '>' or c == '<' or c == '^' or c == 'v':
            cars.append([[x, y], [c, 0], [0, 0]])


#nv = list(map(lambda x: x[0], v))
#print(get(v, [7, 1]))

count = 0
while True:
    pos_array = []
    idx = []
    for car in cars:
        #old_pos = [car[0][0], car[0][1]]
        new_pos(car)

        if list(map(lambda x: x[0], cars)).count(car[0]) > 1:
            print(car[0])
            for i in range(0, len(cars)):
                if list(map(lambda o: o[0], cars)).count(cars[i][0]) > 1:
                    idx.append(i)
                idx.sort(key=lambda x: x, reverse=True)
                for i in idx:
                    cars.pop(i)

        track = get(v, car[0])
        if track:
            new_vel(car, track)
    if len(idx) > 0:
        idx.sort(key=lambda x: x, reverse=True)
        for i in idx:
            cars.pop(i)
        print(idx, cars)




    """
    c_pos = list(map(lambda x: x[2], cars))
    if len(list(filter(lambda x: c_pos.count(x[2]) > 1, cars))) > 0:
        print(list(filter(lambda x: c_pos.count(x[2]) > 1, cars)))
    le = len(cars)
    cars = list(filter(lambda x: c_pos.count(x[2]) < 2, cars))
    if le != len(cars):
        print('2', le, len(cars))

    c_pos = list(map(lambda x: x[0], cars))
    if len(list(filter(lambda x: c_pos.count(x[0]) > 1, cars))) > 0:
        print(list(filter(lambda x: c_pos.count(x[0]) > 1, cars)))
    le = len(cars)
    cars = list(filter(lambda x: c_pos.count(x[0]) < 2, cars))
    if le != len(cars):
        print('0', le, len(cars))
    """
    #print(len(cars))
    if len(cars) == 1:
        print(cars)
        exit()
    count += 1

# 69,67

print(pos)

"""
123,18
54,36
122,69
104,49
24,102
19,85
32,107
83,46
71,123

"""
"""
for y in range(0, len(data)):
    x = 0
    while True:
        x = find(data[y], '\\', x)
        if x >= 0:
            print(x, y)
            break
"""

#print(data[0].index('\\'))
