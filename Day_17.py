import re


def is_in(v, e):
    try:
        v.index(e)
        return True
    except ValueError:
        return False


def initialization():
    f = open('Input/input_day_17_test.txt', 'r')
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


def print_matrix():
    for i in range(0, max_row):
        for j in range(494, max_col):
            print(matrix[i][j], end='', flush=True)
        print()


def check_empty(target, dv):
    global matrix, max_col, max_row
    dx, dy = dv
    x, y = target
    x, y = x + dx, y + dy
    return matrix[y][x] == '.' or matrix[y][x] == '|'


def init_values():
    global right, left, down, matrix, max_col, max_row, data
    right, left, down = [1, 0], [-1, 0], [0, 1]
    data = create_vector(initialization())
    max_col = max(data, key=lambda x: x[0])[0] + 2
    max_row = max(data, key=lambda x: x[1])[1] + 4
    matrix = [['.' for _ in range(0, max_col)] for _ in range(0, max_row)]
    for v in data:
        col, row = v
        matrix[row][col] = '#'


def step(target, dv):
    global matrix, right, left, down, max_row
    dx, dy = dv
    x, y = target
    matrix[y][x] = '|'
    try:
        if dy == 0 and check_empty(target, down):
            step(target, down)
            return
        elif dy == 1 and not check_empty(target, down):
            step(target, left)
            step(target, right)
            return
        elif dy == 0 and not check_empty(target, dv):
            return
        step([x + dx, y + dy], dv)
    except IndexError:
        return


def fill():
    step([500, 0], [0, 0])
    get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
    pool = list(filter(lambda x: x != [], [get_indexes('|', x) for x in matrix]))
    index = len(pool) - 1
    
    if index < max_row - 1:
        for x in pool[index]:
            matrix[index][x] = '~'
        fill()
        

init_values()
fill()
print_matrix()
