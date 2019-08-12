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
	

def print_val_b(b):
	for y in range(size_y):
		for x in range(size_x):
			score = steps[y][x]
			if [x, y] == [target_x, target_y]:
				print(f"{score:03d}", end='^')
			elif [x, y] in b:
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


def initialization():
	global depth, target, size
	target = [14, 400]
	target = [14, 796]
	target = [14, 22]
	target = [14, 785]
	x, y = target
	size = x + 15, y + 15
	depth = 5355
	depth = 510
	depth = 4080
	
	
def set_static(tools):
	global steps, target_x, target_y, rows, cols
	global static_tools, max_score
	static_tools = tools.copy()
	p_ar = [[[0, 0], 0]]
	ntype = [[[0, 0], 0]]
	# iterate([tourch], p_ar, ntype, 40)
	max_score = 99999 #1101
	# steps = [[max_score for _ in f] for f in tourch]
	# steps[0][0] = 0
	# rows, cols = len(steps), len(steps[0])
	# print(searching([tourch, climbing], [[0, 0]]))
	steps = [[max_score for _ in f] for f in tourch]
	# equipments = [[[] for _ in f] for f in tourch]
	steps[0][0] = 0
	target_x, target_y = target
	rows, cols = len(steps), len(steps[0])
	print(searching([tourch, climbing, neiter], [[0, 0]]))
	# print(searching(tourch, [[0, 0]]))
	# print(searching(climbing, [[0, 0]]))


def searching(initial_fields, initial_positions):
	global max_score
	#max_score = 1101
	borders = []

	while initial_positions:#steps[target_y][target_x] == max_score:
		# if steps[target_y][target_x] < max_score:
		# 	max_score = steps[target_y][target_x]
		# 	print(max_score)
		
		if steps[target_y][target_x] < max_score:
			max_score = steps[target_y][target_x]
			print(max_score)
			
		for field in [tourch, neiter, climbing]:
			#positions = borders.copy()
			positions = initial_positions.copy()
			koord = []
			#for x, y in positions:
			while positions:
				x, y = positions.pop(0)
				# if [x, y] in borders:
				# 	borders.remove([x, y])
				# print(len(initial_positions))
				if not field[y][x]:
					continue
				for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
					p = a, b = [x + dx, y + dy]
					if not rows > b >= 0 or not cols > a >= 0:
						continue
					
					if field[b][a]:
						score = steps[y][x] + 1
						
						if score <= steps[b][a]:
							steps[b][a] = score

							# if p in borders and score < steps[b][a]:
							# 	borders.remove(p)
							
							if (p not in positions and p not in initial_positions) or score < steps[b][a]:
								positions.append(p)
								
					else:
						score = steps[y][x] + 8
						if score <= steps[b][a] and p not in initial_positions:
							steps[b][a] = score
							if p not in borders:
								borders.append(p)
		initial_positions = borders.copy()
		borders = []
		# print(initial_positions)
		# print_val_b(initial_positions)
	return steps[target_y][target_x]


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
