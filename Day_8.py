import itertools
import re
from functools import reduce


class Node:
    def __init__(self, array_data):
        print(array_data)
        self.array_data = array_data
        self.child_nodes_entries = array_data[0]
        self.metadata_entries = array_data[1]
        if self.child_nodes_entries == 0:
            self.metadata = array_data[2:2 + self.metadata_entries]
            self.array_data = self.array_data[2 + self.metadata_entries:]
            return

        self.node = Node(self.array_data[2:])
        self.array_data = self.node.array_data


def func(ar, s):
    #while len(ar) > 0:
        nc = ar[0]
        me = ar[1]
        #ar = ar[2:]
        print([nc, me], ar[2:])

        if nc == 0 or len(ar) == me:
            ar = ar[2:]
            print(':', ar, ar[:me])
            return ar, s + sum(ar[:me])
        ar, s = func(ar[2:], s)



f = open('Input/input_test.txt', 'r')
data = f.read()
f.close()

ar = list(map(lambda n: int(n), data.split(' ')))
#ar, s = func(ar, 0)
print(func(ar, 0))
exit()

s = 0
nc = ar[0]
me = ar[1]
me_ar = ar[len(ar) - me:]
s = sum(me_ar)
ar = ar[2:len(ar) - me]
print([nc, me], ar, me_ar)


while len(ar) > 0:
    print(ar)
    nc = ar[0]
    me = ar[1]
    ar = ar[2:]
    if nc == 0:
        me_ar = ar[:me]
        ar = ar[me:]
        s += sum(me_ar)
        print([nc, me], ar, me_ar)

print(s)
