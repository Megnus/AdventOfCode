import copy
import sys

import numpy as np
# 799 >
# 1147 <
# 1101 <
# 1078?
# 1092 Seng





def erosion_level(geologic_index):
	return (geologic_index + depth) % 20183


def geological_index(v, erosions):
	x, y = v

	if v == (0, 0):
		print(v)
		return 0
	if v == (target_x, target_y):
		print(v)
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
	for y in range(size_y):
		for x in range(size_x):
			score = steps[y][x]
			print(f"{score:03d}", end=' ')
		print()
	print()
	

def print_val_b(scoresheet, vec):
	for y in range(size_y):
		for x in range(size_x):
			score = scoresheet[y][x]
			score = score if score < 999 else 000
			if [x, y] == [target_x, target_y]:
				print(f"{score:03d}", end='*')
			elif [x, y] in vec:
				print(f"{score:03d}", end='_')
			else:
				print(f"{score:03d}", end=' ')
		print()
	print()
	
	
def print_type(types):
	t = ['.', '=', '|']
	for y in range(size_y):
		for x in range(size_x):
			if [x, y] == target:
				print('T', end=' ')
			else:
				print(t[types[y][x]], end=' ')
		print()
	print()


def initialization_(n):
	global depth, target, size
	target_1 = [10, 10]
	target_2 = [6, 22]
	#target_3 = [14, 785]
	target_3 = [7, 60]
	target_4 = [14, 796]
	depth_4 = 5355
	depth_3 = 4080
	depth_2 = 4080
	depth_1 = 510
	target_ar = [target_1, target_2, target_3, target_4]
	depth_ar = [depth_1, depth_2, depth_3, depth_4]
	target = target_ar[n]
	depth = depth_ar[n]
	x, y = target
	size = x + 5, y + 5


def initialization():
	initialization_(2)
	

def set_static(tools):
	global steps, target_x, target_y, rows, cols
	global static_tools, max_score
	static_tools = tools.copy()

	max_score = 99999 #1101
	steps = [[max_score for _ in f] for f in tourch]
	steps[0][0] = 0
	target_x, target_y = target
	rows, cols = len(steps), len(steps[0])
	scoresheet = [[max_score for _ in f] for f in tourch]
	scoresheet[0][0] = 0
	searching(tourch, [[0, 0]], copy.deepcopy(scoresheet), 0)
	# print(searching(tourch, [[0, 0]]))
	# print(searching(climbing, [[0, 0]]))
	#testing(scoresheet.copy(), 1)
	#tester = [[tourch[y][x] and neiter[y][x] for x in range(size_x)] for y in range(size_y)]
	# print('\ntester')
	# for y in range(size_y):
	# 	for x in range(size_x):
	# 		if [x, y] == target:
	# 			print('T', end=' ')
	# 		else:
	# 			print('.' if climbing[y][x] else 'x', end='')
	# 			print('.' if neiter[y][x] else 'x', end=' ')
	# 	print()
	# print()


def testing(scoresheet, d):
	if d > 8:
		return
	print('before', d)
	print_val_b(scoresheet.copy(), [])
	scoresheet[0][0] = d
	testing(copy.deepcopy(scoresheet), d + 1)
	print('after: ', d)
	print_val_b(scoresheet, [])


def searching(field, positions, scoresheet, d):
	global max_score
	borders = []
	init_border = copy.deepcopy(positions)
	if d > 10:
		#print('max_score % 8')
		return

	for x, y in positions:
		# if d > (max_score - (abs(x - target_x) + abs(y - target_y))) / 8:
		# 	continue
		
		if not field[y][x] or scoresheet[y][x] + abs(x - target_x) + abs(y - target_y) > max_score:
			continue

		for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
			p = a, b = [x + dx, y + dy]

			if not rows > b >= 0 or not cols > a >= 0:
				continue
			
			# x - target_x + y - target_y
			if field[b][a] and scoresheet[b][a] > scoresheet[y][x] + 1:
				scoresheet[b][a] = scoresheet[y][x] + 1
				positions.append(p)
			elif scoresheet[b][a] >= scoresheet[y][x] + 8 and not field[b][a]:
				scoresheet[b][a] = scoresheet[y][x] + 8
				borders.append(p)
	
	if tourch == field:
		print('tourch', ' depth: ', d, end='\n')
	if climbing == field:
		print('climbing' ' depth: ', d, end='\n')
	if neiter == field:
		print('neiter', ' depth: ', d, end='\n')
	
	if scoresheet[target_y][target_x] < max_score:
		max_score = scoresheet[target_y][target_x]
		
		print('MAX Score: ', max_score, 'depth: ', d)
		
	
	print('  score: ', max_score)
	
	print_val_b(copy.deepcopy(scoresheet), borders)
	print([field[y][x] for x, y in borders if field[y][x]])
	input()
	
	for x, y in positions:
		scoresheet[y][x] = max_score
	
	if not borders:
		return
	
	for field in [tourch, climbing, neiter]:
		searching(field, copy.deepcopy(borders), copy.deepcopy(scoresheet), d + 1)
	
	#print_val_b(copy.deepcopy(scoresheet), borders)

	# for field in [tourch, neiter, climbing]:
	# 	if borders:
	# 		searching(field, borders.copy(), scoresheet.copy(), d + 1)

# https://www.reddit.com/r/adventofcode/comments/a8i1cy/2018_day_22_solutions/


x1 = [[(0, 0, 0), 0, None], [(0, 0, 1), sys.maxsize, None], [(0, 0, 2), sys.maxsize, None]]
y1 = [[(1, 0, 0), sys.maxsize, None], [(1, 0, 1), sys.maxsize, None], [(1, 0, 2), sys.maxsize, None]]
z1 = [[(0, 1, 0), sys.maxsize, None], [(0, 1, 1), sys.maxsize, None], [(0, 1, 2), sys.maxsize, None]]

c = 5
nodes = []
node = [(0, 0, 0), 0, None]
for dx, dy, dz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, 2):
	pos, _, _ = node
	x, y, z = pos
	pos = x + dx, y + dy, z + dz
	node = [pos, c, None]
	nodes.append(node)
	nodes.sort(key=lambda x: x[1])
	c -= 1

print(nodes)
exit()



initialization()
size_x, size_y = size
global target_x, target_y
target_x, target_y = target
max_x, max_y = size_x + 1, size_y + 1
erosions = [[0 for x in range(size_x)] for y in range(size_y)]

for x in range(size_x):
	for y in range(size_y):
		erosions[y][x] = erosion_level(geological_index((x, y), erosions))
		
types = [[erosions[y][x] % 3 for x in range(size_x)] for y in range(size_y)]
calc = [[erosions[y][x] % 3 for x in range(target_x + 1)] for y in range(target_y + 1)]
result_1 = sum([sum(x) for x in calc])
print("Result part 1: ", result_1)

# walk = [0, tools[y][x]]
# set1 = {0, 1}
# set2 = {3, 2}
# tup1 = set1.intersection(set2)

#area = [[erosions[y][x] % 3 for y in range(size_y)] for x in range(size_x)]
area = [[erosions[y][x] % 3 for x in range(size_x)] for y in range(size_y)]
print_type(area)
# print_type(area)

# area = [[erosions[y][x] % 3 for x in range(size_x)] for y in range(size_y)]
# sys.maxsize
tools = [[set(requierd_tool(area[y][x])) for y in range(size_y)] for x in range(size_x)]

steps_new = [[0 for y in range(size_y)] for x in range(size_x)]

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

tourch = [[[x, y] == [0, 0] or [x, y] == target or area[y][x] == 0 or area[y][x] == 2 for x in range(size_x)] for y in range(size_y)]
climbing = [[[x, y] != [0, 0] and [x, y] != target and (area[y][x] == 0 or area[y][x] == 1) for x in range(size_x)] for y in range(size_y)]
neiter = [[[x, y] != [0, 0] and [x, y] != target and (area[y][x] == 1 or area[y][x] == 2) for x in range(size_x)] for y in range(size_y)]

border = [[False for x in range(size_x)] for y in range(size_y)]
new_border = [[False for x in range(size_x)] for y in range(size_y)]
fields = [[False for x in range(size_x)] for y in range(size_y)]

print(tourch)
print(size_x, size_y)
print('\nall')

for y in range(size_y):
	for x in range(size_x):
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

set_static(tools)


