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

    rows = in_data.splitlines()
    while True:
        if '' in rows:
            rows = rows[rows.index('') + 1:]
        else:
            break

    val = [[int(y) for y in x.split(' ')] for x in rows]
    return list(zip(re_before_int, re_operation_int, re_after_int)), val


def operation(input_val):
    global fc, fc_name
    in_reg, operation_reg, out_reg = input_val
    val_0, val_a, val_b, val_3 = operation_reg
    out_reg_val = out_reg[val_3]

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
        1 if val_a == in_reg[val_b] else 0,
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

    indices = [i for i, x in enumerate(fc) if x == out_reg_val]
    return val_0, [fc_name[x] for x in indices]


def calculate_number_of_opcodes(opcodes):
    dictionary = {}
    for x in opcodes:
        dictionary[x[0]] = list(set(dictionary[x[0]] + x[1]) if x[0] in dictionary else [])
    filtered_list = [x[0] for x in dictionary.items() if len(x[1]) >= 3]
    filtered_opcodes = [x for x in opcodes if x[0] in filtered_list]
    return len(filtered_opcodes)


def solve_opcodes():
    global x, opcodes
    op_code_dic = {}
    for x in opcodes:
        op_code_dic[x[0]] = list(set(op_code_dic[x[0]]) & set(x[1]) if x[0] in op_code_dic else x[1])
    opcodes = sorted(op_code_dic.items(), key=lambda x: x[0])
    while [x for x in opcodes if len(x[1]) > 1]:
        for q in [x for x in opcodes if len(x[1]) == 1]:
            for t in opcodes:
                if q[1][0] in t[1] and len(t[1]) > 1:
                    t[1].remove(q[1][0])


def operation_(reg, op, dec):
    code, a, b, c = op
    oper = [
        ('addr', reg[a] + reg[b]),
        ('addi', reg[a] + b),
        ('mulr', reg[a] * reg[b]),
        ('muli', reg[a] * b),
        ('banr', reg[a] & reg[b]),
        ('bani', reg[a] & b),
        ('borr', reg[a] | reg[b]),
        ('bori', reg[a] | b),
        ('setr', reg[a]),
        ('seti', a),
        ('gtir', 1 if a > reg[b] else 0),
        ('gtri', 1 if reg[a] > b else 0),
        ('gtrr', 1 if reg[a] > reg[b] else 0),
        ('eqir', 1 if a == reg[b] else 0),
        ('eqri', 1 if reg[a] == b else 0),
        ('eqrr', 1 if reg[a] == reg[b] else 0)
    ]

    reg[c] = [x[1] for x in oper if dec[code] in x[0]][0]
    return reg


# PART 1
op_values, test_values = initialization()
opcodes = [operation(x) for x in op_values]
result_1 = calculate_number_of_opcodes(opcodes)


# PART 2
solve_opcodes()
dec = {}
for x in opcodes:
    dec[x[0]] = x[1][0]
reg = [0, 0, 0, 0]
result_2 = [operation_(reg, x, dec) for x in test_values][-1:][0][0]

print("Result part 1: ", result_1)
print("Result part 2: ", result_2)
