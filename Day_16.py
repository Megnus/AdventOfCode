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


values = initialization()

