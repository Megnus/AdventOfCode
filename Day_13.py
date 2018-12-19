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
def new_pos(cart):
    M = {'v': [0, 1], '<': [-1, 0], '>': [1, 0], '^': [0, -1]}
    cart[0][0] += M[cart[1][0]][0]
    cart[0][1] += M[cart[1][0]][1]
    cart[2] = True
    return cart


def new_vel(cart, track_p):
    M = {'\\': {'v': '>', '<': '^', '>': 'v', '^': '<'},
         '/': {'v': '<', '<': 'v', '>': '^', '^': '>'}}
    S = ['>', '^', '<', 'v']
    N = [1, 0, -1]
    if track_p == '+':
        index = S.index(cart[1][0]) + N[cart[1][1]]
        index = 3 if index < 0 else index % 4
        cart[1][0] = S[index]
        cart[1][1] = (cart[1][1] + 1) % 3
    else:
      cart[1][0] = M[track_p][cart[1][0]]
    return cart


f = open('Input/input_test.txt', 'r')
f = open('Input/input_day_13.txt', 'r')

data = f.read()
f.close()
data = data.splitlines()

v = []
carts = []
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        c = data[y][x]
        if c == '\\' or c == '/' or c == '+':
            v.append([[x, y], c])
        elif c == '>' or c == '<' or c == '^' or c == 'v':
            carts.append([[x, y], [c, 0], True])

collisions = []
while True:
    for cart in sorted(carts):
        if not cart[2]:
            continue
        new_pos(cart)
        if list(map(lambda c: c[0], carts)).count(cart[0]) > 1:
            collisions.append(cart[0])
            for c in carts:
                if c[0] == cart[0]:
                    c[2] = False
            break
        track = get(v, cart[0])
        if track:
            new_vel(cart, track)
    carts = list(filter(lambda c: c[2], carts))
    if len(carts) == 1:
        break

print('First collision:', collisions[0], 'Last position:', carts[0][0])

