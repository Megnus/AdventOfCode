def initialization():
	global depth, target
	target = (10, 10)
	depth = 510
	depth = 4080
	target = (14, 785)


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


initialization()
target_x, target_y = target
max_x, max_y = target_x + 1, target_y + 1
erosions = [[0 for x in range(max_x)] for y in range(max_y)]

for x in range(max_x):
	for y in range(max_y):
		erosions[y][x] = erosion_level(geological_index((x, y), erosions))

types = [[erosions[y][x] % 3 for x in range(max_x)] for y in range(max_y)]
result_1 = sum([sum(x) for x in types]) - types[target_x][target_y]
print("Result part 1: ", result_1)
# print("Result part 2: ", result_2)
