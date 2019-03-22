import re


def initialization():
    f = open('Input/input_day_17.txt', 'r')
    in_data = f.read()
    f.close()
    in_data_x = re.findall('x=.+y=.+', in_data)
    in_data_y = re.findall('y=.+x=.+', in_data)
    out_data_x = [re.findall('(\d+)', x) for x in in_data_x]
    out_data_y = [re.findall('(\d+)', y) for y in in_data_y]
    out_data_x = [[int(x[0]), int(x[1]), int(x[2])] for x in out_data_x]
    out_data_y = [[int(y[0]), int(y[1]), int(y[2])] for y in out_data_y]
    return out_data_x, out_data_y


def create_vector(data_xy):
    data_x, data_y = data_xy
    vec_x = [[[x[0], y] for y in range(x[1], x[2] + 1)] for x in data_x]
    vec_y = [[[x, y[0]] for x in range(y[1], y[2])] for y in data_y]
    return [x for y in vec_x + vec_y for x in y]


def print_streams():
    for i in range(0, 100):
        for j in range(480, max_col):
            print(space[i][j], end='', flush=True)
        print()


def check_empty(target, dv):
    dx, dy = dv
    x, y = target
    x, y = x + dx, y + dy
    return space[y][x] == '.' or space[y][x] == '|'


def init_values():
    global right, left, down, halt, space, max_col, max_row, min_row, data, start
    right, left, down, halt = [1, 0], [-1, 0], [0, 1], [0, 0]
    start = [[500, 0], down]
    data = create_vector(initialization())
    max_col = max(data, key=lambda x: x[0])[0] + 1
    max_row = max(data, key=lambda x: x[1])[1] + 1
    min_row = min(data, key=lambda x: x[1])[1]
    space = [['.' for _ in range(0, max_col)] for _ in range(0, max_row)]
    for v in data:
        col, row = v
        space[row][col] = '#'


def create_stream_layer(position, direction):
    col_direction, _ = direction
    col, row = position
    while space[row][col] == '|':
        col -= col_direction
    if space[row][col] == '#':
        col, row = position
        while space[row][col] == '|':
            space[row][col] = '~'
            col -= col_direction
            

def pour_water():
    while '|' not in space[max_row - 1]:
        streams = [start]
        while streams:
            try:
                stream = streams.pop()
                position, direction = stream
                col_direction, row_direction = direction
                col, row = position
                if check_empty(position, halt):
                    space[row][col] = '|'
                    if row_direction == 0 and check_empty(position, down):
                        streams.append([position, down])
                    elif row_direction == 1 and not check_empty(position, down):
                        streams.append([position, right])
                        streams.append([position, left])
                    elif row_direction == 0 and not check_empty(position, direction):
                        create_stream_layer(position, direction)
                    else:
                        position = [col + col_direction, row + row_direction]
                        stream = [position, direction]
                        streams.append(stream)
            except IndexError:
                continue


def count_water():
    sum_streams = sum([len([x for x in y if x == '|']) for y in space]) - min_row
    sum_water = sum([len([x for x in y if x == '~']) for y in space])
    return sum_streams + sum_water, sum_water
    

init_values()
pour_water()
result_1, result_2 = count_water()
print("Result part 1: ", result_1)
print("Result part 2: ", result_2)
