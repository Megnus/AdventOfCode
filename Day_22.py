import sys


def initialization():
	global depth, target, size
	depth = 4080
	target = (14, 785)
	target = (10, 10)
	x, y = target
	size = x + int(x / 2) + 1, y + int(y / 2) + 1
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
	for x in range(size_x):
		for y in range(size_y):
			score, _ = steps[y][x]
			print(f"{score:03d}", end=' ')
		print()


def print_type(types):
	t = ['.', '=', '|']
	for x in range(size_x):
		for y in range(size_y):
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
tools = [[set(requierd_tool(area[y][x])) for x in range(size_x)] for y in range(size_y)]

t = ['.', '=', '|']
for x in range(size_x):
	for y in range(size_y):
		print(t[area[y][x]], tools[y][x], end=' ')
	print()
print()
steps = [[[999, set()] for y in range(size_y)] for x in range(size_x)]

dv = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = (0, 0)
steps[0][0] = [0, tools[0][0]]

new_score = True
while new_score:
	new_score = False
	for x in range(size_x - 1):
		for y in range(size_y - 1):
			# print(t[area[y][x]], tools[y][x], end=' ')
			for dx, dy in dv:
				print(steps[y][x])
				score, tool = steps[y][x]
				px, py = x + dx, y + dy
				print(steps[py][px])
				print(tool.intersection(tools[py][px]))
				g = input();
				
				if px > size_x or py > size_y or px < 0 or py < 0:
					continue
				
				new_tool = tools[py][px]
				tool_in_hand = tool.intersection(new_tool)
				print("tool_in_hand", tool_in_hand, "[px, py]", [px, py], "tool", tool, "new_tool", new_tool)
				g = input();
				
				if tool_in_hand:
					score += 1
				else:
					score += 8
					tool_in_hand = new_tool
				
				if score < steps[py][px][0]:
					steps[py][px] = [score, tool_in_hand]
					new_score = True
			
				print(steps[py][px])
				g = input();
				
		# print()

print()
print_val()













# print("Result part 2: ", result_2)
