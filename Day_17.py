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


data = create_vector(initialization())
print(data)
max_col = max(data, key=lambda x: x[0])[0] + 2
max_row = max(data, key=lambda x: x[1])[1] + 4
print(max_col, max_row)
'''[col, row]#>'''
matrix = [['.' for col in range(0, max_col)] for row in range(0, max_row)]
for v in data:
    col = v[0]
    row = v[1]
    matrix[row][col] = '#'
    
print(matrix)
for i in range(0, max_row):
    for j in range(494, max_col):
        print(matrix[i][j], end='', flush=True)
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
