def is_in(v, e):
    try:
        v.index(e)
        return True
    except ValueError:
        return False


def initialization_input(file_name):
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
            print('x' if is_in(markers, [x, y]) else p[x][y], end='')
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


def get_enemy_player_type(player):
    return 'G' if player[0] == 'E' else 'E'


def get_legal_moves(position):
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
    positions = get_legal_moves(position)
    depth = 0
    while len(positions) > 0:
        depth += 1
        new_positions = []
        for position in positions:
            x, y = position
            if distance[x][y] < 0:
                distance[x][y] = depth
                new_positions += get_legal_moves(position)
        positions = new_positions
    return distance


def get_closest_position(player):
    _, player_position, _, _ = player
    distance = get_distance_matrix(player_position)
    enemy_player_type = get_enemy_player_type(player)
    enemy_players = get_players_by_type(enemy_player_type)
    enemy_players_moves = []
    for enemy_player in enemy_players:
        enemy_player_position = enemy_player[1]
        enemy_player_moves = get_legal_moves(enemy_player_position)
        for enemy_player_move in enemy_player_moves:
            enemy_players_moves.append(enemy_player_move)
    get_sorted_positions(enemy_players_moves)
    enemy_players_moves = list(filter(lambda x: distance[x[0]][x[1]] > 0, enemy_players_moves))
    min_distance_position = []
    if enemy_players_moves:
        min_distance_position = min(enemy_players_moves, key=lambda x: distance[x[0]][x[1]])
    return min_distance_position


def get_path(player):
    directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    player_type, player_position, hp, active = player
    target_position = get_closest_position(player)
    if not target_position:
        return []
    distance = get_distance_matrix(player_position)
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
    sx, sy = player[1]
    tx, ty = target_pos
    player_type = p[sx][sy]
    p[sx][sy] = '.'
    p[tx][ty] = player_type
    player[1] = [tx, ty]


def get_neighbour_enemy_players(player, players):
    directions = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    player_type, player_position, hp, active = player
    enemy_player_type = get_enemy_player_type(player)
    x, y = player_position
    source_moves = list(map(lambda d: [x + d[0], y + d[1]], directions))
    player_list = list(filter(lambda x: x[1] in source_moves, players))
    player_list = list(filter(lambda x: x[0] == enemy_player_type, player_list))
    get_sorted_players(player_list)
    return player_list


def get_neighbour_enemy_player(player, players):
    active_players = list(filter(lambda x: x[3], players))
    opp_players = get_neighbour_enemy_players(player, active_players)
    if len(opp_players) == 0:
        return None
    opp_player = min(opp_players, key=lambda x: x[2])
    return opp_player


def attack_enemy_player(opp_player, attack_hp):
    global p
    if opp_player:
        opp_player[2] -= attack_hp
        if opp_player[2] <= 0:
            opp_player[3] = False
            x, y = opp_player[1]
            p[x][y] = '.'


def battle_ended(players):
    goblins_alive = 'G' in [x[0] for x in players if x[3]]
    elf_alive = 'E' in [x[0] for x in players if x[3]]
    return not (goblins_alive and elf_alive)


def battle(elf_attack):
    round = 0
    attack_map = {'E': elf_attack, 'G': 3}
    players = get_players()

    while not battle_ended(players):
        for player in players:
            # Validate present player
            player_active = player[3]
            if not player_active:
                continue

            # Move present player
            if not get_neighbour_enemy_player(player, players):
                path = get_path(player)
                if path:
                    first_step = path[1]
                    move_player(player, first_step)

            # Attack enemy player
            enemy_player = get_neighbour_enemy_player(player, players)
            get_enemy_player_type(player)
            attack = attack_map[player[0]]
            attack_enemy_player(enemy_player, attack)

            # Update round and check battle end
            if player == players[-1]:
                round += 1
            elif battle_ended(players):
                break

        players = list(filter(lambda x: x[3], players))
        get_sorted_players(players)

    won = list(set([player[0] for player in players]))[0]
    hp = sum(player[2] for player in players)
    score = round * hp
    num_of_elfs = [x[0] for x in players].count('E')
    return score, won, num_of_elfs


def get_battle_score():
    initialization()
    result = battle(3)
    return result[0]


def get_elf_survival_battle_score():
    initialization()
    number_of_elfs = [x[0] for x in get_players()].count('E')
    max_elf_attack = 10000
    for attack in range(3, max_elf_attack):
        initialization()
        result = battle(attack)
        if result[2] == number_of_elfs:
            return result[0]
    return None


def initialization():
    global p, w, h
    p, w, h = initialization_input('Input/input_day_15.txt')


print('Part 1:', get_battle_score())
print('Part 2:', get_elf_survival_battle_score())