import _thread
import tools
import math
import time


def recover_secret(triplets):
    word = ''
    letters = set([j for sub in triplets for j in sub])
    while letters:
        word += {sum([x.index(a) for x in triplets if a in x]): a for a in letters}[0]
        triplets = [list(filter(lambda x: x is not word[-1], sub)) for sub in triplets]
        letters.remove(word[-1])
    return word


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


def get_pos(p, d):
    global directions, v
    pos = []
    test = False
    if [p[0], p[1]] == [2, 3]:
        print('..................................')
    for m in directions:
        np = [p[0] + m[0], p[1] + m[1], d]
        if [p[0], p[1]] == [2, 3]:
            print(np, '.............. +++++++++++ ....................')
            print( v[np[0]][np[1]], '.............. +++++++++++ ....................')

        t = v[np[0]][np[1]]
        if test:
            print(np)
        if t[0] == '.':
            pos.append(np)
    if [p[0], p[1]] == [2, 3]:
        print(pos, '..............POSOPSPSPSP....................')

    return pos


def get_all_pos(p):
    global v
    occ = get_pos(p)
    q = True
    while q:
        q = False
        #occ = get_pos(m)
        print('occ: ', occ)
        occ = get_all_pos(m)
        for m in occ:
            if not tools.is_in(occ, m): # and get_pos(v, b[1]):
                occ.append(m)
                q = True
    return occ


def is_not_in(vec, p):
    occ = list(map(lambda x: [x[0], x[1]], vec))
    return not tools.is_in(occ, [p[0], p[1]])


def print_distance_matrix(distance):
    for x in range(0, w):
        for y in range(0, h):
            val = distance[x][y]
            print('-' if val < 0 else val, end=' ')
        print()


def distance_calc(pos):
    global v
    distance = [[-1 for x in range(w)] for y in range(h)]
    x, y = pos
    distance[x][y] = 0
    positions = get_move(pos)
    depth = 0
    for i in range(0, 15):
        depth += 1
        new_positions = []
        for pos in positions:
            x, y = pos
            if distance[x][y] < 0:
                distance[x][y] = depth
                new_positions.append(pos)
        positions = []
        for pos in new_positions:
            positions += get_move(pos)

    print_distance_matrix(distance)
    return distance


def get_spec(eg):
    global v, w, h
    p = []
    for col in v:
        for ele in col:
            if eg == ele[0]:
                p.append(ele)
    return p


def get_move(p):
    global v, directions
    pos = []
    for m in directions:
        np = [p[0] + m[0], p[1] + m[1]]
        t = v[np[0]][np[1]]
        if t[0] == '.':
            pos.append(t[1])
        if t[1] != np:
            print(t[1], np)
    return pos


def get_moves(p):
    pos = []
    for m in p:
        pos += get_move(m)
    return pos


def fib(n):
    a, b = 0, 1
    for i in range(n - 1):
        c = a + b
        a, b = b, c
    return c


def calc_primes(prod):
    primes = []
    i = 1
    while i <= prod:
        i += 1
        if prod % i == 0:
            prod //= i
            primes.append(i)
            i = 1
    return primes


print(fib(35))

num = math.log(9227465 * math.sqrt(5), 0.5 + math.sqrt(5) / 2)
print(num)
p = calc_primes(4321412341253325454645762431352653475325421354364)
print(p)
exit()

exit()
directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
v = init()
w, h = len(v), len(v[0])


distance_calc([2, 3])

exit()
#g = get_spec('G')
#e = get_spec('E')
"""
    pos = get_moves(extract(g))
    print_data(v, pos)
"""

"""
    positions = rebase([2, 2], [], 0)
    positions = sorted(positions, key=lambda x: x[2])
    points = set([x[2] for x in positions])
    __positions = list(filter(lambda x: x[2] == 13, positions))
    
    _positions = list(filter(lambda x: x[2] == 1, positions))
    _positions = [[x[0], x[1]] for x in _positions]
    print_data(v, _positions)
    exit()
    for p in positions:
        print(p[2], ':', [p[0], p[1]])
"""

# Create two threads as follows
try:
    for i in range(0, 200):
        _thread.start_new_thread(calc_primes, 4321412341253325454645762431352653475325421354364, )
        time.sleep(1)
except:
    print("Error: unable to start thread")

while True:
    pass
