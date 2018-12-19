import itertools
import re
from functools import reduce


def output(vec):
    vec_str = list(map(lambda x: str(x), vec))
    vec_str[a] = '(' + vec_str[a] + ')'
    vec_str[b] = '[' + vec_str[b] + ']'
    print(' '.join(vec_str))


v, a, b = [3, 7], 0, 1
n = 9
# output(v)

while len(v) < n + 11:
    c = v[a] + v[b]
    c1 = c % 10
    c2 = int((c - c1) / 10)
    v += [c2, c1] if c2 > 0 else [c1]
    a += (v[a] + 1)
    b += (v[b] + 1)
    a %= len(v)
    b %= len(v)
    # output(v)

v = list(map(lambda x: str(x), v))
result = ''.join(v[n:n + 10])
print(result)

v, a, b = [3, 7], 0, 1
right = [5, 1, 3, 4, 0, 1]
off = len(right)

while v[-off:] != right and v[-off - 1: -1] != right:
    c = v[a] + v[b]
    c1 = c % 10
    c2 = int((c - c1) / 10)
    v += [c2, c1] if c2 > 0 else [c1]
    length = len(v)
    a = (a + (v[a] + 1)) % length
    b = (b + (v[b] + 1)) % length

result = len(v) - off
result -= 0 if v[-off:] == n else 1
print(result)


