import sys


def initialization():
	global depth, target, size
	target = (14, 785)
	target = (10, 10)
	x, y = target
	size = x + 10, y + 10
	depth = 4080
	depth = 510


def erosion_level(geologic_index):
	return (geologic_index + depth) % 20183


def geological_index(v, erosions):
	x, y = v
	if v == (0, 0):
		return 0
	if y == 0:
		return x * 16807
	if x == 0:
		return y * 48271
	return erosions[y][x - 1] * erosions[y - 1][x]


# rocky (.), wet (=), narrow (|)
# torch, climbing, neither

# rocky (.) = climbing, tourch (0, 1)
# wet (=) = climbing, neither (2, 3)
# narrow (|) = tourch, neither (0, 2)

# tourch   : . |
# climbing : . =
# neiter   : = |

def time_calc(tool, type):
	if not tool == 2 and type == 0:
		return tool, 0
	if not tool == 0 and type == 1:
		return tool, 0
	if not tool == 1 and type == 2:
		return tool, 0
	return 7


def requierd_tool(type):
	if type == 0:
		return 0, 1
	if type == 1:
		return 1, 2
	if type == 2:
		return 0, 2


def print_val():
	for x in range(size_x):
		for y in range(size_y):
			score, _ = steps_new[y][x]
			print(f"{score:03d}", end=' ')
		print()


def print_type(types):
	t = ['.', '=', '|']
	for x in range(size_y):
		for y in range(size_x):
			print(t[types[y][x]], end=' ')
		print()
	print()

initialization()
size_x, size_y = size
target_x, target_y = target
max_x, max_y = target_x + 1, target_y + 1
erosions = [[0 for x in range(size_x)] for y in range(size_y)]

for x in range(size_x):
	for y in range(size_y):
		erosions[y][x] = erosion_level(geological_index((x, y), erosions))

types = [[erosions[y][x] % 3 for x in range(max_x)] for y in range(max_y)]
result_1 = sum([sum(x) for x in types]) - types[target_y][target_x]
print("Result part 1: ", result_1)

# walk = [0, tools[y][x]]
# set1 = {0, 1}
# set2 = {3, 2}
# tup1 = set1.intersection(set2)

area = [[erosions[y][x] % 3 for y in range(size_y)] for x in range(size_x)]
print_type(area)

# area = [[erosions[y][x] % 3 for x in range(size_x)] for y in range(size_y)]
# sys.maxsize
tools = [[set(requierd_tool(area[y][x])) for y in range(size_x)] for x in range(size_y)]

steps_new = [[0 for y in range(size_x)] for x in range(size_y)]

t = ['.', '=', '|']
# for x in range(size_y):
# 	for y in range(size_x):
# 		print(t[area[y][x]], tools[y][x], end=' ')
# 		steps_new[y][x] = [999, tools[y][x]]
# 		# print(steps_new)
# 	print()
# print()
# steps = [[[999, set()] for y in range(size_y)] for x in range(size_x)]

dv = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = (0, 0)
# steps[0][0] = [0, tools[0][0]]
steps_new[0][0] = [0, {0}]

# rocky (.), wet (=), narrow (|)
# torch, climbing, neither

# rocky (.) = climbing, tourch (0, 1)
# wet (=) = climbing, neither (2, 3)
# narrow (|) = tourch, neither (0, 2)

# tourch   : . |
# climbing : . =
# neiter   : = |

tourch = [[area[y][x] == 0 or area[y][x] == 2 for y in range(size_x)] for x in range(size_y)]
climbing = [[area[y][x] == 0 or area[y][x] == 1 for y in range(size_x)] for x in range(size_y)]
neiter = [[area[y][x] == 1 or area[y][x] == 2 for y in range(size_x)] for x in range(size_y)]

print(tourch)
print(size_x, size_y)

for y in range(size_y):
	for x in range(size_x):
		if [x, y] == [14, 785]:
			print('T', end=' ')
		else:
			print('.' if tourch[y][x] else 'x', end=' ')
	print()
print()

scores = [[-1 for y in range(size_x)] for x in range(size_y)]
scores[0][0] = 0

changed = True
while changed:
	changed = False
	for y in range(size_y - 1):
		for x in range(size_x - 1):
			if scores[y][x] > -1:
				for dx, dy in dv:
					if y + dy >= 0 and x + dx >= 0:
						if scores[y + dy][x + dx] < 0 and tourch[y + dy][x + dx]:
							scores[y + dy][x + dx] = scores[y][x] + 1
							changed = True


for y in range(size_y):
	for x in range(size_x):
		print(f"{scores[y][x]:03d}", end=' ')
	print()
print()

input()

for y in range(size_y):
	for x in range(size_x):
		if [x, y] == [14, 785]:
			print('T', end=' ')
		else:
			print('.' if climbing[y][x] else 'x', end=' ')
	print()
print()
input()

for y in range(size_y):
	for x in range(size_x):
		if [x, y] == [14, 785]:
			print('T', end=' ')
		else:
			print('.' if neiter[y][x] else 'x', end=' ')
	print()
print()










# print("Result part 2: ", result_2)
