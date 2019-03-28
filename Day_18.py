import copy


def initialization():
    global fields, max_row, max_col
    f = open('Input/input_day_18.txt', 'r')
    in_data = f.read()
    f.close()
    fields = [list(x) for x in in_data.splitlines()]
    max_row = len(fields)
    max_col = len(fields[0])


def get_adjacent(point):
    px, py = point
    sq = [[px + x, py + y] for x in range(-1, 2) for y in range(-1, 2)]
    sq.remove(point)
    sq = list(filter(lambda v: 0 <= v[0] < max_row and 0 <= v[1] < max_col, sq))
    sp = [fields[y][x] for x, y in sq]
    return sp


def get_new_item(point):
    ar = get_adjacent(point)
    x, y = point
    if fields[y][x] == '.' and ar.count('|') >= 3:
        return '|'
    elif fields[y][x] == '|' and ar.count('#') >= 3:
        return '#'
    elif fields[y][x] == '#' and ar.count('#') >= 1 and ar.count('|') >= 1:
        return '#'
    elif fields[y][x] == '#':
        return '.'
    return fields[y][x]


def create_fields():
    return [[get_new_item([x, y]) for x in range(0, max_col)] for y in range(0, max_row)]


def itr_fields():
    global fields
    ten_minutes_index = 10 - 1
    index = 1000000000 - 1
    fields_array = list()
    while True:
        fields = create_fields()
        if fields in fields_array:
            length = len(fields_array)
            repetative_index = fields_array.index(fields)
            equivalent_index = (index - length) % (length - repetative_index)
            break
        fields_array.append(copy.deepcopy(fields))
    return fields_array[ten_minutes_index], fields_array[equivalent_index + repetative_index]
    

def get_result(fields):
    flatten = [y for x in fields for y in x]
    return flatten.count('|') * flatten.count('#')


initialization()
part_1_fields, part_2_fields = itr_fields()
print("Result part 1: ", get_result(part_1_fields))
print("Result part 2: ", get_result(fields))
