import itertools
import re
from functools import reduce


def contains(array, val):
    try:
        return array.index(val) >= 0
    except ValueError:
        return False


c = 1  # global variable


def add():
    global c
    c = c + 2  # increment c by 2
    print(c)


add()