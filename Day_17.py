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
    vec_x = [[[x[0], y] for y in range(x[1], x[2])] for x in data_x]
    vec_y = [[[x, y[0]] for x in range(y[1], y[2])] for y in data_y]
    return [x for y in vec_x + vec_y for x in y]


data = create_vector(initialization())
print(data)
