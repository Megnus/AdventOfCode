def initialization():
	f = open('Input/input_day_20.txt', 'r')
	in_data = f.read()
	f.close()
	# re_before = re.sub('\(.+?\)', '', in_data)
	# re_before = re.sub('^[A-Z]', '', 'EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)')
	# re_before = re.findall('[A-Z]+', in_data)
	# re_before = re.findall('[\(|\)|\|]', in_data)
	# re_before = re.findall('\(.+?\)', in_data)
	# re_before = re.findall('(?<=Before:\s\[).+(?=\])', in_data)
	# re_before = re.findall('(?<=\^).+(?=\$)', in_data)[0]
	# re_before1 = re.findall('^.+?(?=[\(|\||\)])', re_before)
	# article = re.sub('^.+?(?=[\(|\|])', '', re_before)
	# re_before1 = re.findall('^.+?(?=[\(|\||\)])', article)
	# re.findall('(?<=\^).+(?=\$)', in_data)[0]
	return in_data


directions = {'E': (1, 0), 'W': (-1, 0), 'N': (0, 1), 'S': (0, -1)}
path = []


def explore(string, start, end_char):
	global path
	checkpoint = start
	index = 0
	while index < len(string):
		index += 1
		char = string[index]
		if char in directions:
			dx, dy = directions[char]
			x, y = checkpoint
			checkpoint = (x + dx, y + dy)
			path.append([char, checkpoint])
			checkpoint = (x + 2 * dx, y + 2 * dy)
			path.append([char, checkpoint])
		elif char == '(':
			index += explore(string[index:], checkpoint, ')')
		elif char == '|':
			checkpoint = start
		elif char == end_char:
			return index
	return 0


def print_fields(fields):
	for x in fields:
		print(x)


data = initialization()
end_char = '$'
explore(list(data), (0, 0), end_char)
koordinates = [e[1] for e in path]
x_max = max([p[0] for p in koordinates])
x_min = min([p[0] for p in koordinates])
y_max = max([p[1] for p in koordinates])
y_min = min([p[1] for p in koordinates])

start = [-x_min, -y_min]
koordinates = [start] + [[x[0] + start[0], x[1] + start[1]] for x in koordinates]
fields = [[' # ' for col in range(x_max - x_min + 1)] for row in range(y_max - y_min + 1)]
distances = [[0 for col in range(x_max - x_min + 1)] for row in range(y_max - y_min + 1)]

for col, row in koordinates:
	fields[row][col] = '.'

tracks = [start]
doors = []
steps = 1
fields[row][col] = f"{steps:03d}"

while tracks:
	steps += 1
	positions = []
	for col, row in tracks:
		for v in directions.values():
			dx, dy = v
			try:
				x, y = col + dx, row + dy
				if fields[y][x] == '.' and x >= 0 and y >= 0:
					fields[y][x] = 'x'
					if steps % 2 == 0:
						doors += [int(steps / 2)]
					positions.append([x, y])
			except IndexError:
				pass
	tracks = positions

flat_list = max([int(item) for sublist in fields for item in sublist if item.isdigit()])
last = max(doors)
size = len(list(filter(lambda x: x >= 1000, doors)))
print("Result part 1: ", last)
print("Result part 2: ", size)
