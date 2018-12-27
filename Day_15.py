import itertools
import re
from functools import reduce
import tools


def extract(u):
    global p
    return list(map(lambda x: x[1], u))


def init():
    f = open('Input/input_day_15.txt', 'r')
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


def print_data(u):
    global w, h, p
    print()
    for y in range(0, h):
        for x in range(0, w):
            if tools.is_in(u, [x, y]):
                print('x', end='')
            else:
                print(v[x][y][0], end='')
        print()


def get_all_pos(p):
    occ = get_move(p)
    q = True
    while q:
        q = False
        for o in occ:
            for s in get_move(o):
                if not tools.is_in(occ, s): # and get_pos(v, b[1]):
                    occ.append(s)
                    q = True
    return occ


def get_spec(eg):
    global v, w, h
    pos = []
    for col in v:
        for ele in col:
            if eg == ele[0]:
                pos.append(ele)
    return pos


def get_neighbours(player):
    global p, opponents_map
    position = player[1]
    x, y = position
    pl_type = player[0]
    op_pl_type = opponents_map[pl_type]
    neighbours = []
    for direction in directions:
        dx, dy = direction
        value = v[x + dx][y + dy][0]
        if value == op_pl_type:
            neighbours.append([x + dx, y + dy])
    return neighbours


def get_players():
    global p, w, h
    players = []
    for y in range(h):
        for x in range(w):
            if v[x][y][0] != '.' and v[x][y][0] != '#':
                player = v[x][y]
                player.append(200)
                players.append(player)
    return players


def get_spec_targets(eg):
    move = []
    global p, w, h
    positions = list(map(lambda x: x[1], get_spec(eg)))
    for position in positions:
        move += get_move(position)
    return move


def get_move(p):
    global v, directions
    pos = []
    for m in directions:
        np = [p[0] + m[0], p[1] + m[1]]
        t = v[np[0]][np[1]]
        if t[0] == '.':
            pos.append(t[1])
    return pos


def print_distance_matrix(distance):
    for y in range(h):
        for x in range(w):
            value = distance[x][y]
            print('-' if value < 0 else value, end=' ')
        print()


def calc_distance(position):
    global p, w, h
    x, y = position
    distance = [[-1 for i in range(h)] for j in range(w)]
    distance[x][y] = 0
    positions = get_move(position)
    depth = 0
    while len(positions) > 0:
        depth += 1
        new_positions = []
        for position in positions:
            x, y = position
            if distance[x][y] < 0:
                distance[x][y] = depth
                new_positions += get_move(position)
        positions = new_positions
    return distance


def get_path(source, target):
    distance = calc_distance(source)
    x, y = target
    value = distance[x][y]
    path = [target]
    while value > 0:
        value -= 1
        for direction in directions:
            x, y = target
            dx, dy = direction
            x, y = x + dx, y + dy
            if distance[x][y] == value:
                target = [x, y]
                path.append(target)
                break
    path.reverse()
    return path


def get_nearest(source, targets):
    distance = calc_distance(source)
    dist_pos = list(map(lambda x: distance[x[0]][x[1]], targets))
    # min_val = reduce(lambda x, y: x if x < y else y, dist_pos)
    dist_pos = list(filter(lambda x: x >= 0, dist_pos))
    if len(dist_pos) == 0:
        return []
    min_val = min(dist_pos)

    min_dist_pos = list(filter(lambda x: distance[x[0]][x[1]] == min_val, targets))
    min_dist_pos.sort(key=lambda x: x[1]*10000 + x[0])
    return min_dist_pos[0]


def get_nearest_by_multiple_sources(sources, targets):
    # targets = get_moves(targets)
    nearest = []
    for source in sources:
        target = get_nearest(source, targets)
        x, y = target
        distance = calc_distance(source)
        value = distance[x][y]
        nearest.append([source, target, value])
    nearest.sort(key=lambda x: x[2])
    source, target, val = nearest[0]
    return [source, target]


def get_moves(p):
    pos = []
    for e in p:
        pos += get_move(e)
    return pos


# Variables
directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
opponents_map = {'G': 'E', 'E': 'G'}
v = init()
w, h = len(v), len(v[0])

# Get Elfs
elfs = get_spec('E')

# Get Goblins (Targets)
goblins = get_spec('G')

# Get target from Goblins
em = get_spec_targets('G')
#print_data(em)

# In range
pos = get_moves(extract(goblins))
#print_data(pos)

# Reachable
occ = get_all_pos(extract(elfs)[0])
occ = tools.intersection(pos, occ)

# Get next move
source = [2, 2]
# nearest = get_nearest(source, [[5, 3], [5, 7], [6, 7], [7, 2], [6, 3], [1, 6]])

# Get all players
#print_data([])

attack = 25

players = get_players()
# print_data(players)
round = 0
while len(set(list(map(lambda x: x[0], players)))) > 1:
    round += 1

    players = tools.sort_players_by_reading_order(players)

    for i in range(len(players)):
        try:
            pl = players[i]
        except IndexError:
            continue

        if not pl:
            continue

        pl_type, pl_pos, pl_hp = pl
        op_pl_type = opponents_map[pl_type]

        op_player_pos = get_neighbours(pl)

        if len(op_player_pos) > 0:

            players_filter = list(filter(lambda x: x, players))
            op_player = list(filter(lambda x: tools.is_in(op_player_pos, x[1]), players_filter))
            op_player = min(op_player, key=lambda x: x[2])
            op_player[2] -= attack if op_player[0] == 'G' else 3
            if op_player[2] <= 0:
                x, y = op_player[1]
                v[x][y][0] = '.'
                players_filter = list(filter(lambda x: x, players))
                players = list(map(lambda x: None if x[2] <= 0 else x, players_filter))
            continue

        players_filter = list(filter(lambda x: x, players))
        op_pl = list(filter(lambda x: x[0] == op_pl_type, players_filter))
        op_pl = extract(op_pl)
        targets_op_pl = get_moves(op_pl)

        if len(targets_op_pl) == 0:
            continue

        target = get_nearest(pl_pos, targets_op_pl)

        if len(target) == 0:
            continue

        path = get_path(pl_pos, target)
        fx, fy = path[0]
        tx, ty = path[1]
        val = v[fx][fy][0]
        v[fx][fy][0] = '.'
        v[tx][ty][0] = val
        players[i] = [pl_type, [tx, ty], pl_hp]

        op_player_pos = get_neighbours(players[i])

        if len(op_player_pos) > 0:
            players_filter = list(filter(lambda x: x, players))
            op_player = list(filter(lambda x: tools.is_in(op_player_pos, x[1]), players_filter))
            op_player = min(op_player, key=lambda x: x[2])
            op_player[2] -= attack if op_player[0] == 'G' else 3
            if op_player[2] <= 0:
                x, y = op_player[1]
                p[x][y][0] = '.'
                players_filter = list(filter(lambda x: x, players))
                players = list(map(lambda x: None if x[2] <= 0 else x, players_filter))
            continue
    #players = list(filter(lambda x: x, players))
    players = tools.sort_players_by_reading_order(players)
    if round > 28:
        print(players)
    # print('Round:', round)
    # print_data([])
    # print(players)

points = sum(list(map(lambda x: x[2], players)))
print_data([])
print('Round:', round, 'hp:', points)
print('points', (round - 1) * points)
print(players)
print(len(players))
# print_data([])
# 227460, 230136, 232812, 42255