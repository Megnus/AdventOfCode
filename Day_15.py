import itertools
import re
from functools import reduce
import tools


def extract(u):
    global v
    return list(map(lambda x: x[1], u))


def init():
    f = open('Input/input_test.txt', 'r')
    in_data = f.read()
    f.close()
    in_data = in_data.splitlines()
    in_data = [list(x) for x in in_data]
    height = len(in_data)
    width = len(in_data[0])
    p = []
    for x in range(0, width):
        p.append([])
        for y in range(0, height):
            p[x].append([in_data[y][x], [x, y]])
    return p

"""
def print_data(v):
    global w, h
    for y in range(0, h):
        for x in range(0, w):
            print(v[x][y][0], end='')
        print()
"""


def print_data(v, u):
    global w, h
    for y in range(0, h):
        for x in range(0, w):
            if tools.is_in(u, [x, y]):
                print('x', end='')
            else:
                print(v[x][y][0], end='')
        print()

"""
def get_pos(v, p):
    global move
    move_found = False
    for m in move:
        np = [p[0] + m[0], p[1] + m[1]]
        t = v[np[0]][np[1]][0]
        if t == '.':
            v[np[0]][np[1]][0] = 'x'
            move_found = True
    return move_found
"""

def get_all_pos(v, p):
    get_pos(v, p)
    q = True
    while q:
        q = False
        for a in v:
            for b in a:
                if b[0] == 'x' and not tools.is_in(v, b[]) # and get_pos(v, b[1]):
                    q = True


def get_spec(eg):
    global v, w, h
    pos = []
    for col in v:
        for ele in col:
            if eg == ele[0]:
                pos.append(ele)
    return pos


def get_move(p):
    global v, move
    pos = []
    for m in move:
        np = [p[0] + m[0], p[1] + m[1]]
        t = v[np[0]][np[1]]
        if t[0] == '.':
            pos.append(t[1])
    return pos


def get_moves(p):
    pos = []
    for e in p:
        pos += get_move(e)
    return pos


move = [[0, -1], [-1, 0], [1, 0], [0, 1]]
v = init()
w, h = len(v), len(v[0])
g = get_spec('G')
e = get_spec('E')
pos = get_moves(extract(g))

print_data(v, pos)

get_all_pos(v, [2,2])
print_data(v, [])

