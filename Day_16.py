import re


def is_in(v, e):
    try:
        v.index(e)
        return True
    except ValueError:
        return False


def initialization():
    f = open('Input/input_day_16.txt', 'r')
    in_data = f.read()
    f.close()
    re_before = re.findall('(?<=Before:\s\[).+(?=\])', in_data)
    re_before_trim = [x.replace(' ', '').split(',') for x in re_before]
    re_before_int = [[int(y) for y in x] for x in re_before_trim]

    re_operation = re.findall('(?<=\]\n)\d+\s.+?(?=\nAfter)', in_data, flags=re.S | re.M)
    re_operation_int = [[int(y) for y in x.split(' ')] for x in re_operation]

    re_after = re.findall('(?<=After:\s\s\[).+(?=\])', in_data)
    re_after_trim = [x.replace(' ', '').split(',') for x in re_after]
    re_after_int = [[int(y) for y in x] for x in re_after_trim]

    return list(zip(re_before_int, re_operation_int, re_after_int))


def oper(values):
    in_reg, oper, out_reg = values
    reg_0, reg_1, reg_2, reg_3 = in_reg
    val_0, val_a, val_b, val_3 = oper
    out_reg_0, out_reg_1, out_reg_2, out_reg_3 = out_reg

    fc = [
        in_reg[val_a] + in_reg[val_b],
        in_reg[val_a] + val_b,
        in_reg[val_a] * in_reg[val_b],
        in_reg[val_a] * val_b,
        in_reg[val_a] & in_reg[val_b],
        in_reg[val_a] & val_b,
        in_reg[val_a] | in_reg[val_b],
        in_reg[val_a] | val_b,
        in_reg[val_a],
        val_a,
        1 if val_a > in_reg[val_b] else 0,
        1 if in_reg[val_a] > val_b else 0,
        1 if in_reg[val_a] > in_reg[val_b] else 0,
        1 if val_a == reg_2 else 0,
        1 if in_reg[val_a] == val_b else 0,
        1 if in_reg[val_a] == in_reg[val_b] else 0
    ]

    fc_name = [
        'addr',
        'addi',
        'mulr',
        'muli',
        'banr',
        'bani',
        'borr',
        'bori',
        'setr',
        'seti',
        'gtir',
        'gtri',
        'gtrr',
        'eqir',
        'eqri',
        'eqrr',
    ]

    print(fc)
    indices = [i for i, x in enumerate(fc) if x == out_reg_2]
    print(indices)
    print([fc_name[x] for x in indices])


def addi(values):
    in_val, oper, out_val = values
    a, b, c = in_val
    out_temp = [a, b, a * b]


def addi(values):
    in_val, oper, out_val = values
    a, b, c = in_val
    out_temp = [a, b, a * b]


values = initialization()
oper([[3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]])

