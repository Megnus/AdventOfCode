import copy


def print_fields():
    print()
    for i in fields:
        for j in i:
            print(j, end='', flush=True)
        print()


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
    # print(list(zip(sq, sp)))
    # for i in sq:
    #     for j in i:
    #         print(j, end='', flush=True)
    #     print()


def get_new_item(point):
    # items = ['.', '|', '#']
    # ar = get_adjacent(point)
    # index = items.index(point)
    # func = [
    #     lambda:
    # ]
    # new_fields = fields.copy()
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


def create_fields_by_time(time):
    global fields
    f_ar = list()
    for t in range(1, time + 1):
        fields = create_fields()
        # f_ar.append(fields.deepcopy())
        #print('Time: ', t)
        #print_fields()


def itr_fields():
    global fields
    f_ar = list()
    while True:
        fields = create_fields()
        if fields in f_ar:
            last_index = len(f_ar)
            index = f_ar.index(fields)
            # 1000000000
            idx = (1000000000 - 1 - last_index) % (last_index - index)
            print('INDEX: ', f_ar.index(fields))
            return f_ar[idx + index]
        # f_ar.append(fields.deepcopy())
        f_ar.append(copy.deepcopy(fields))
        #print('Time: ', t)
        #print_fields()


def get_result():
    # create_fields_by_time(5)
    flatten = [y for x in fields for y in x]

    # nf = copy.deepcopy(fields)
    # ar = ['x', nf]
    # nf[0][0] = '~'
    # print(fields[0][0])
    # print(nf[0][0])
    # print(nf == fields)
    # print('index: ', fields in ar)
    # nf[0][0] = '|'
    # print(nf == fields)
    # print('index: ', ar.index(fields))


    return flatten.count('|') * flatten.count('#')


#initialization()
#create_fields_by_time(10)
#print(get_result())


initialization()
fields = itr_fields()
get_result()
#count_adjacent([3, 9])
# fields = get_new_item([7, 0])
# print_fields()
# create_fields_by_time(10)


print(get_result())

# 191196

# > 42818
# > 45216
# > 49749
# != 194449
# ? 195160
