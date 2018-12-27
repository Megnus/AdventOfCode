import itertools
import re
from functools import reduce


def output(vec):
    vec_str = list(map(lambda x: str(x), vec))
    vec_str[a] = '(' + vec_str[a] + ')'
    vec_str[b] = '[' + vec_str[b] + ']'
    print(' '.join(vec_str))


p, a, b = [3, 7], 0, 1
n = 9
# output(v)

while len(p) < n + 11:
    c = p[a] + p[b]
    c1 = c % 10
    c2 = int((c - c1) / 10)
    p += [c2, c1] if c2 > 0 else [c1]
    a += (p[a] + 1)
    b += (p[b] + 1)
    a %= len(p)
    b %= len(p)
    # output(v)

p = list(map(lambda x: str(x), p))
result = ''.join(p[n:n + 10])
print(result)

p, a, b = [3, 7], 0, 1
right = [5, 1, 3, 4, 0, 1]
off = len(right)

while p[-off:] != right and p[-off - 1: -1] != right:
    c = p[a] + p[b]
    c1 = c % 10
    c2 = int((c - c1) / 10)
    p += [c2, c1] if c2 > 0 else [c1]
    length = len(p)
    a = (a + (p[a] + 1)) % length
    b = (b + (p[b] + 1)) % length

result = len(p) - off
result -= 0 if p[-off:] == n else 1
print(result)


