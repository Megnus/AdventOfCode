import itertools
import re
from functools import reduce
import tools


def init(file_name):
    f = open(file_name, 'r')
    in_data = f.read()
    f.close()
    in_data = in_data.splitlines()
    in_data = [list(x) for x in in_data]
    height = len(in_data)
    width = len(in_data[0])
    p = []
    for x in range(width):
        p.append([])
        for y in range(height):
            p[x].append(in_data[y][x])
    return p, width, height


def print_field_markers(markers):
    global w, h, p
    for y in range(h):
        for x in range(w):
            print('x' if tools.is_in(markers, [x, y]) else p[x][y], end='')
        print()


def print_distance(distance):
    global w, h, p
    for y in range(h):
        for x in range(w):
            string = "0" + str(distance[x][y])
            print(string[-2:], end=' ')
        print()


def print_field():
    print_field_markers([])


def get_players():
    global w, h, p
    players = []
    for y in range(h):
        for x in range(w):
            element = p[x][y]
            if element == 'E' or element == 'G':
                players.append([element, [x, y], 200, True])
    get_sorted_players(players)
    return players


def get_players_by_type(player_type):
    return list(filter(lambda x: x[0] == player_type, get_players()))


def get_sorted_positions(positions):
    positions.sort(key=lambda x: 10000 * x[1] + x[0])
    return positions


def get_sorted_players(players):
    players.sort(key=lambda x: 10000 * x[1][1] + x[1][0])
    return players


def get_opposite_player(player_type):
    return 'G' if player_type == 'E' else 'E'


def get_leagal_moves(position):
    global p
    x, y = position
    directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    move = []
    for direction in directions:
        dx, dy = direction
        if p[x + dx][y + dy] == '.':
            move.append([x + dx, y + dy])
    return move


def get_distance_matrix(position):
    global p, w, h
    x, y = position
    distance = [[-1 for y in range(h)] for x in range(w)]
    distance[x][y] = 0
    positions = get_leagal_moves(position)
    depth = 0
    while len(positions) > 0:
        depth += 1
        new_positions = []
        for position in positions:
            x, y = position
            if distance[x][y] < 0:
                distance[x][y] = depth
                new_positions += get_leagal_moves(position)
        positions = new_positions
    return distance


def get_closest_position(player):
    player_type, player_position, hp, active = player
    distance = get_distance_matrix(player_position)
    opp_player_type = get_opposite_player(player_type)
    opp_players = get_players_by_type(opp_player_type)
    opp_players_moves = []
    for opp_player in opp_players:
        op_player_position = opp_player[1]
        op_player_moves = get_leagal_moves(op_player_position)
        for op_player_move in op_player_moves:
            opp_players_moves.append(op_player_move)
    get_sorted_positions(opp_players_moves)
    if not opp_players_moves:
        return []
    min_distance_position = min(opp_players_moves, key=lambda x: distance[x[0]][x[1]])
    return min_distance_position


def get_path(player):
    directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    player_type, player_position, hp, active = player
    target_position = get_closest_position(player)
    if not target_position:
        return []
    distance = get_distance_matrix(player_position)
    print_distance(distance)
    print(target_position)
    x, y = target_position
    value = distance[x][y]
    path = [target_position]
    while value > 0:
        value -= 1
        for direction in directions:
            x, y = target_position
            dx, dy = direction
            x, y = x + dx, y + dy
            if distance[x][y] == value:
                target_position = [x, y]
                path.append(target_position)
                break
    path.reverse()
    return path


def move_player(player, target_pos):
    global p
    print(player)
    sx, sy = player[1]
    tx, ty = target_pos
    player_type = p[sx][sy]
    p[sx][sy] = '.'
    p[tx][ty] = player_type
    player[1] = [tx, ty]


def get_neighbour_opp_players(player, players):
    directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    player_type, player_position, hp, active = player
    opp_player_type = get_opposite_player(player_type)
    x, y = player_position
    source_moves = list(map(lambda d: [x + d[0], y + d[1]], directions))
    player_list = list(filter(lambda x: x[1] in source_moves, players))
    player_list = list(filter(lambda x: x[0] == opp_player_type, player_list))
    get_sorted_players(player_list)
    return player_list


def get_neighbour_opp_player(player, players):
    opp_players = get_neighbour_opp_players(player, players)
    if len(opp_players) == 0:
        return None
    opp_player = min(opp_players, key=lambda x: x[2])
    return opp_player


def attack_opp_player(opp_player, attack_hp):
    global p
    if opp_player:
        opp_player[2] -= attack_hp
        if opp_player[2] <= 0:
            opp_player[3] = False
            x, y = opp_player[1]
            p[x][y] = '.'


def is_battle_over(players):
    return 'G' in [x[0] for x in players] and 'E' in [x[0] for x in players]


p, w, h = init('Input/input_test_1.txt')
print_field()

players = get_players()
while is_battle_over(players):
    for player in players:
        player_active = player[3]
        if not player_active:
            continue

        active_players = list(filter(lambda x: x[2], players))
        opp_player = get_neighbour_opp_player(player, active_players)
        # attack_opp_player(opp_player, 3)

        if not opp_player:
            path = get_path(player)
            if path:
                first_step = path[1]
                move_player(player, first_step)

        opp_player = get_neighbour_opp_player(player, players)
        attack_opp_player(opp_player, 3)
        print(players)
    players = list(filter(lambda x: x[3], players))
    print_field()
