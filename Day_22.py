import numpy as np


def initialization():
	global depth, target, size
	target = [10, 10]
	target = (14, 785)
	x, y = target
	size = x + 5, y + 20
	depth = 510
	depth = 4080


def erosion_level(geologic_index):
	return (geologic_index + depth) % 20183


def geological_index(v, erosions):
	x, y = v

	if v == (0, 0):
		return 0
	if v == target:
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
	for x in range(size_x):
		for y in range(size_y):
			if [x, y] == target:
				print('T', end=' ')
			else:
				print(t[types[y][x]], end=' ')
		print()
	print()


def set_static(tools):
	global counter
	counter = 0

	global static_tools
	static_tools = tools.copy()
	p_ar = [[[0, 0], 0]]
	ntype = [[[0, 0], 0]]
	iterate([tourch], p_ar, ntype, 14)


def iterate(tools, p_ar, ntype, iter):
	b_ar = []
	for tool in tools:
		# print('iter: ', 20 - iter)
		while p_ar:
			p, s = p_ar.pop(0)
			for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
				x, y = p
				x, y = x + dx, y + dy
				if 0 <= x < size_x and 0 <= y < size_y:
					sc = [sx for v, sx in ntype if v == [x, y]]
					sc = sc[0] if sc else 999
					if tool[y][x]:
						if s + 1 < sc:
							p_ar = [[v, s] for v, s in p_ar if v != [x, y]]
							ntype = [[v, s] for v, s in ntype if v != [x, y]]
							p_ar.append([[x, y], s + 1])
							ntype.append([[x, y], s + 1])
					else:
						if s + 8 < sc:
							p_ar = [[v, s] for v, s in p_ar if v != [x, y]]
							ntype = [[v, s] for v, s in ntype if v != [x, y]]
							b_ar.append([[x, y], s + 8])
							ntype.append([[x, y], s + 8])

					p_occ.append([x, y])

		p_ar = b_ar.copy()
		b_ar.clear()
		score_v = [s for v, s in ntype if v == target]
		if score_v:
			print('=', static_tools.index(tool))
			print(':', score_v[0])
			return
		else:
			new_tools = static_tools.copy()
			new_tools.remove(tool)
			if iter > 0:
				iterate(new_tools, p_ar.copy(), ntype, iter - 1)
			return



initialization()
size_x, size_y = size
global target_x, target_y
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
# print_type(area)

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
climbing = [[[x, y] != target and (area[y][x] == 0 or area[y][x] == 1) for y in range(size_x)] for x in range(size_y)]
neiter = [[[x, y] != target and (area[y][x] == 1 or area[y][x] == 2) for y in range(size_x)] for x in range(size_y)]
border = [[False for y in range(size_x)] for x in range(size_y)]
new_border = [[False for y in range(size_x)] for x in range(size_y)]
fields = [[False for y in range(size_x)] for x in range(size_y)]

print(tourch)
print(size_x, size_y)
print('\nall')

for x in range(size_y):
	for y in range(size_x):
		if [x, y] == target:
			print(area[y][x], end='_')
		else:
			print(area[y][x], end=' ')
		# if [x, y] == [10, 10]:
		# 	print('T', end=' ')
		# elif area[y][x] == 0 or area[y][x] == 1:
		# 	print('.', end=' ')
		# else:
		# 	print('x', end=' ')
	print()
print()

print('\ntourch')
for y in range(size_y):
	for x in range(size_x):
		if [x, y] == target:
			print('T', end=' ')
		else:
			print('.' if tourch[y][x] else 'x', end=' ')
	print()
print()

print('climbing')
for y in range(size_y):
	for x in range(size_x):
		if [x, y] == target:
			print('.' if climbing[y][x] else 'x', end='<')
		else:
			print('.' if climbing[y][x] else 'x', end=' ')
	print()
print()

scores = [[-1 for y in range(size_x)] for x in range(size_y)]
scores[0][0] = 0

print()
print('nieter')
for y in range(size_y):
	for x in range(size_x):
		if [x, y] == target:
			print('T', end=' ')
		else:
			print('.' if neiter[y][x] else 'x', end=' ')
	print()
print()


fields[0][0] = True
tool = tourch
changed = True
changed1 = True
tools = [tourch]

# print(np.array(p_ar).unravel_index(p_ar.argmax(), p_ar.shape))

p_ar = [[[0, 0], 0]]
p_occ = [[0, 0]]
ntype = [[[0, 0], 0]]
b_ar = []
tools = [tourch, neiter, climbing]
tools = []
for tool in tools:
	print('tool')
	while p_ar:
		# print(len(ntype))
		p, s = p_ar.pop(0)
		for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
			x, y = p
			x, y = x + dx, y + dy
			if 0 <= x < size_x and 0 <= y < size_y:
				sc = [sx for v, sx in ntype if v == [x, y]]
				sc = sc[0] if sc else 999
				if tool[y][x]:
					if s + 1 < sc:
						p_ar = [[v, s] for v, s in p_ar if v != [x, y]]
						ntype = [[v, s] for v, s in ntype if v != [x, y]]
						p_ar.append([[x, y], s + 1])
						ntype.append([[x, y], s + 1])
				else:
					if s + 8 < sc:
						p_ar = [[v, s] for v, s in p_ar if v != [x, y]]
						ntype = [[v, s] for v, s in ntype if v != [x, y]]
						b_ar.append([[x, y], s + 8])
						ntype.append([[x, y], s + 8])

				p_occ.append([x, y])

	# if tool == climbing or True:
	# 	for a in range(size_y - 1):
	# 		for b in range(size_x - 1):
	# 			if [b, a] in [v for v, _ in ntype]:
	# 				score = [s for v, s in ntype if v == [b, a]]
	# 				# print([b, a], score)
	# 				if [b, a] in [[10, 10]]:
	# 					score = [s for v, s in ntype if v == [b, a]]
	# 					# print([b, a], score)
	# 					print(f"_{score[0]:2d}", end=' ')
	# 				else:
	# 					print(f"{score[0]:03d}", end=' ')
	# 			else:
	# 				print(f"{0:03d}", end=' ')
	# 		print()
	# 	print()

	p_ar = b_ar.copy()
	b_ar.clear()
	score_v = [s for v, s in ntype if v == target]
	if score_v:
		print(score_v[0])

tools = [tourch, neiter, climbing]
set_static(tools)
