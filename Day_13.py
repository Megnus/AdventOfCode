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


# car = [[x, y], [v, n] is_moved]
def new_pos(c):
    M = {'v': [0, 1], '<': [-1, 0], '>': [1, 0], '^': [0, -1]}
    c[0][0] += M[c[1][0]][0]
    c[0][1] += M[c[1][0]][1]
    c[2] = True
    return car


def new_vel(car, track_p):
    M = {'\\': {'v': '>', '<': '^', '>': 'v', '^': '<'},
         '/': {'v': '<', '<': 'v', '>': '^', '^': '>'}}
    S = ['>', '^', '<', 'v']
    N = [1, 0, -1]

    if track_p == '+':
        index = S.index(car[1][0]) + N[car[1][1]]
        index = 3 if index < 0 else index % 4
        car[1][0] = S[index]
        car[1][1] = (car[1][1] + 1) % 3
    else:
      car[1][0] = M[track_p][car[1][0]]

    return car


f = open('Input/input_test.txt', 'r')
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
            cars.append([[x, y], [c, 0], True])

collisions = []
while True:
    for car in sorted(cars):
        if not car[2]:
            continue
        new_pos(car)
        if list(map(lambda x: x[0], cars)).count(car[0]) > 1:
            collisions.append(car[0])
            cars = list(map())
            for c in cars:
                if c[0] == car[0]:
                    c[2] = False
            break
        track = get(v, car[0])
        if track:
            new_vel(car, track)
    cars = list(filter(lambda c: c[2], cars))
    if len(cars) == 1:
        break

print('First collision:', collisions, 'Last position:', cars[0][0])

