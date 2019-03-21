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

"""
data = create_vector(initialization())
print(data)
max_col = max(data, key=lambda x: x[0])[0] + 2
max_row = max(data, key=lambda x: x[1])[1] + 4
print(max_col, max_row)
matrix = [['.' for col in range(0, max_col)] for row in range(0, max_row)]
for v in data:
    col, row = v
    matrix[row][col] = '#'
    
print(matrix)
for i in range(0, max_row):
    for j in range(494, max_col):
        print(matrix[i][j], end='', flush=True)
    print()
"""

'''
target = [500, 0]
x, y = target
probe = matrix[y][x]
# probe
while probe == '.' or probe == '|':
    matrix[y][x] = '|'
    x, y = target
    target = [x, y + 1]
    x, y = target
    probe = matrix[y][x]
'''


def print_matrix():
    print()
    global matrix, max_col, max_row
    for i in range(0, max_row):
        for j in range(494, max_col):
            print(matrix[i][j], end='', flush=True)
        print()


def check_empty(target, dv):
    global matrix, max_col, max_row
    dx, dy = dv
    x, y = target
    x, y = x + dx, y + dy
    # print_matrix()
    # print(matrix[y][x], matrix[y][x] == '.' or matrix[y][x] == '|', dv)
   # if x >= max_col or y >= max_row:
       # return False
    
    return matrix[y][x] == '.' or matrix[y][x] == '|'


def init_values():
    global right, left, down, matrix, max_col, max_row, data
    right = [1, 0]
    left = [-1, 0]
    down = [0, 1]

    data = create_vector(initialization())
    print(data)
    max_col = max(data, key=lambda x: x[0])[0] + 2
    max_row = max(data, key=lambda x: x[1])[1] + 4
    print(max_col, max_row)
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
        
    print_matrix()
    
    #print(max(get_inde))
    #if '|' not in matrix[max_row - 1]:
        # break_row = False
        # for i in range(0, max_row):
        #     for j in range(0, max_col):
        #         if matrix[max_row - i - 1][j] == '|':
        #             matrix[max_row - i - 1][j] = '~'
        #             break_row = True
        #     if break_row:
        #         break

   # print_matrix()

#except IndexError:
        #print('calc som shit')

init_values()
# target = [500, 0]
# step(target, [0, 0])
# print_matrix()
# break_row = False
# for i in range(0, max_row):
#     for j in range(494, max_col):
#         if matrix[max_row - i - 1][j] == '|':
#             matrix[max_row - i - 1][j] = '~'
#             break_row = True
#     if break_row:
#         break
# print_matrix()
# target = [500, 0]
# step(target, [0, 0])
# print_matrix()
fill()
print_matrix()
exit()


print()
break_row, found_platou = False
for i in range(0, max_row):
    for j in range(494, max_col):
        if matrix[max_row - i - 1][j] == '#':
            found_platou = True
        if found_platou and matrix[max_row - i - 1][j] == '|':
            matrix[max_row - i - 1][j] = '~'
            break_row = True
    if break_row:
        break

for i in range(0, max_row):
    for j in range(494, max_col):
        print(matrix[i][j], end='', flush=True)
    print()
print()


def itterat(dv_arr):
    dv = [0, 1]
    # dx, dy = dv
    while True:
        x, y = target
        matrix[y][x] = '|'
        for dv in dv_arr:
            dx, dy = dv
            x, y = x + dx, y + dy
            if matrix[y][x] != '.' and matrix[y][x] != '|':
                break
            target = [x, y]


dv = [0, 1]
dx, dy = dv
while True:
    x, y = target
    matrix[y][x] = '|'
    x, y = x + dx, y + dy
    if matrix[y][x] != '.' and matrix[y][x] != '|':
        break
    target = [x, y]

ends = 0
dv = [1, 0]
dx, dy = dv
while True:
    x, y = target
    matrix[y][x] = '|'
    x, y = x + dx, y + dy
    if dy == 0 and ends == 0 and (matrix[y + 1][x] == '.' or matrix[y][x] == '|'):
        if ends == 0:
            target = [dx * -1, 0]
        else:
            target = [0, 1]
        continue
    
    if matrix[y][x] != '.' and matrix[y][x] != '|':
        ends += 1
        break
    target = [x, y]

dv = [-1, 0]
dx, dy = dv
while True:
    x, y = target
    matrix[y][x] = '|'
    x, y = x + dx, y + dy
    if matrix[y][x] != '.' and matrix[y][x] != '|':
        ends + 1
        break
    target = [x, y]

print()
break_row = False
for i in range(0, max_row):
    for j in range(494, max_col):
        if matrix[max_row - i - 1][j] == '|':
            matrix[max_row - i - 1][j] = '~'
            break_row = True
    if break_row:
        break

for i in range(0, max_row):
    for j in range(494, max_col):
        print(matrix[i][j], end='', flush=True)
    print()
print()

'''
Find +
Check best path
    if free down . or |
        go down
    else
        go left and right
        if left and right are blocked then go back with ~ until blocked (# or ~)
        if left or right is blocked terminate the blocked
        go to check best path -> continue until all threads are blocked
        
    
down (. or |) --> if blocked (# or ~) --> two: left and right --> go until blocked (# or ~) -->
if cross path: ~ --> until blocked (# or ~): terminate
'''
