import itertools
import re
from functools import reduce


# List comprehension way
# The list of lists
array = [range(4), range(7)]

# Flatten the lists
flattened_list = [y for x in array for y in x]


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def filter_first_from_second(lst1, lst2):
    lst3 = [x for x in lst1 if x not in lst2]
    return lst3
    # return set(lst1) - set(lst2)


def is_in(v, e):
    try:
        v.index(e)
        return True
    except ValueError:
        return False


def find(vec, elm):
    vec = list(map(lambda x: x[0], vec))
    try:
        return vec.index(elm)
    except ValueError:
        return -1


def get(vec, elm):
    idx = find(vec, elm)
    if idx >= 0:
        return vec[idx][1]


def sort_vector_by_reading_order(vec):
    vec.sort(key=lambda x: str(x[1]) + str(x[0]))


def sort_players_by_reading_order(players):
    players = list(filter(lambda x: x, players))
    players.sort(key=lambda x: x[1][1]*10000 + x[1][0])
    return players


# lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
def get_indexes(val, vec):
    return [i for (y, i) in zip(vec, range(len(vec))) if val == y]
