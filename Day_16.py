import re


def is_in(v, e):
    try:
        v.index(e)
        return True
    except ValueError:
        return False


def initialization():
    global fc, fc_name
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


values = initialization()
opcodes = [operation(x) for x in values]
op_code_dic = {}
for x in opcodes:
    op_code_dic[x[0]] = list(set(op_code_dic[x[0]] + x[1]) if x[0] in op_code_dic else [])

filtered_list = [x[0] for x in op_code_dic.items() if len(x[1]) >= 3]
filtered_opcodes = [x for x in opcodes if x[0] in filtered_list]
result_1 = len(filtered_opcodes)
print(result_1)


op_code_dic = {}
for x in opcodes:
    op_code_dic[x[0]] = list(set(op_code_dic[x[0]]) & set(x[1]) if x[0] in op_code_dic else x[1])

opcodes = sorted(op_code_dic.items(), key=lambda x: x[0])

while [x for x in opcodes if len(x[1]) > 1]:
    for q in [x for x in opcodes if len(x[1]) == 1]:
        for t in opcodes:
            if q[1][0] in t[1] and len(t[1]) > 1:
                t[1].remove(q[1][0])

for x in opcodes:
    print(x)

