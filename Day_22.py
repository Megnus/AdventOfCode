import sys


def initialization():
	global depth, target
	depth = 4080
	target = (14, 785)
	target = (10, 10)
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
	for x in range(max_x):
		for y in range(max_y):
			score, _ = steps[y][x]
			print(f"{score:03d}", end=' ')
		print()


initialization()
target_x, target_y = target
max_x, max_y = target_x + 1, target_y + 1
erosions = [[0 for x in range(max_x)] for y in range(max_y)]

for x in range(max_x):
	for y in range(max_y):
		erosions[y][x] = erosion_level(geological_index((x, y), erosions))

types = [[erosions[y][x] % 3 for x in range(max_x)] for y in range(max_y)]
result_1 = sum([sum(x) for x in types]) - types[target_y][target_x]
print("Result part 1: ", result_1)

#sys.maxsize
tools = [[set(requierd_tool(types[y][x])) for x in range(max_x)] for y in range(max_y)]
steps = [[[999, set()] for x in range(max_x)] for y in range(max_y)]

dv = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = (0, 0)
steps[0][0] = [0, tools[0][0]]
# walk = [0, tools[y][x]]
# set1 = {0, 1}
# set2 = {3, 2}
# tup1 = set1.intersection(set2)

new_score = True
while new_score:
	new_score = False
	for x in range(max_x):
		for y in range(max_y):
			for dx, dy in dv:
				print(x, y)
				score, tool = steps[y][x]
				px, py = x + dx, y + dy
				print([px, py], [dx, dy])
				if px >= max_x or py >= max_y or px < 0 or py < 0:
					continue
				new_tool = tools[py][px]
				tool_in_hand = tool.intersection(new_tool)
				print(tool_in_hand)
				
				if tool_in_hand:
					score += 1
				else:
					score += 8
				
				print(score, steps[py][px])
				if score < steps[py][px][0]:
					steps[py][px] = [score, tool_in_hand]
					new_score = True
				print_val()
				print()
				# g = input()
					#break













# print("Result part 2: ", result_2)
