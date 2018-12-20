import itertools
import re
from functools import reduce


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

