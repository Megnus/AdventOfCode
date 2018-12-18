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
f = open('Input/input_day_13.txt', 'r')
f = open('Input/input_day_13_test.txt', 'r')
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
            cars.append([[x, y], [c, 0]])

#nv = list(map(lambda x: x[0], v))
#print(get(v, [7, 1]))

count = 0
collision = False
while not collision:
    #print(cars[0], get(v, cars[0][0]))
    pos_array = []
    for car in cars:
        if not pos_array and not pos_array.count(car[0]) > 1:
            new_pos(car)
            car_pos = list(map(lambda p: p[0], cars))
        #for p in car_pos:
        if car_pos.count(car[0]) > 1:
            pos_array.append(car[0])
            print(list(map(lambda x: x[0], cars)))
            print(pos_array)
        else:
            track = get(v, car[0])
            if track:
                new_vel(car, track)

    if pos_array:
        print(list(map(lambda x: x[0], cars)))

    cars = list(filter(lambda x: not is_in(pos_array, x[0]), cars))

    if pos_array:
        print(list(map(lambda x: x[0], cars)))
    #print(cars)
    if len(cars) == 1:
        print(cars)
        exit()
    count += 1

# 69,67

print(pos)

#72,117


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
