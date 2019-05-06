import re


def initialization():
	f = open('Input/input_day_20.txt', 'r')
	in_data = f.read()
	f.close()
	print(in_data)
	re_before = re.sub('\(.+?\)', '', in_data)
	re_before = re.sub('^[A-Z]', '', 'EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)')
	re_before = re.findall('[A-Z]+', in_data)
	print(re_before)
	re_before = re.findall('[\(|\)|\|]', in_data)
	print(re_before)
	re_before = re.findall('\(.+?\)', in_data)
	print(re_before)
	
	"""
	#re_before = re.findall('(?<=Before:\s\[).+(?=\])', in_data)
	re_before = re.findall('(?<=\^).+(?=\$)', in_data)[0]
	print(re_before)
	re_before1 = re.findall('^.+?(?=[\(|\||\)])', re_before)
	print(re_before1)
	article = re.sub('^.+?(?=[\(|\|])', '', re_before)
	print(article)
	re_before1 = re.findall('^.+?(?=[\(|\||\)])', article)
	print(re_before1)
	"""
	# return re.findall('(?<=\^).+(?=\$)', in_data)[0]
	return in_data


directions = {'E': (1, 0), 'W': (-1, 0), 'N': (0, 1), 'S': (0, -1)}
path = []


def explore(string, start, end_char):
	global path
	checkpoint = start
	print('')
	index = 0
	while index < len(string):
		index += 1
		char = string[index]
		
		if char in directions:
			dx, dy = directions[char]
			x, y = checkpoint
			checkpoint = (x + dx, y + dy)
			path.append([char, checkpoint])
			checkpoint = (x + 2*dx, y + 2*dy)
			path.append([char, checkpoint])
			print(char, end=' ')
		elif char == '(':
			# path.append(char)
			index += explore(string[index:], checkpoint, ')')
		elif char == '|':
			#path.append(['R', checkpoint])

			checkpoint = start
			# path.append(char)
			print('')
		elif char == end_char:
			# path.append(char)
			print('')
			return index
	return 0


data = initialization()
end_char = '$'
print(list(data))
explore(list(data), (0, 0), end_char)
koordinates = [e[1] for e in path]
x_max = max([p[0] for p in koordinates])
x_min = min([p[0] for p in koordinates])
y_max = max([p[1] for p in koordinates])
y_min = min([p[1] for p in koordinates])
print(x_min, x_max, y_min, y_max)
print(x_max - x_min, y_max - y_min)
print('start: ', -x_min, -y_min)

start = [-x_min, -y_min]
koordinates = [start] + [[x[0] + start[0], x[1] + start[1]] for x in koordinates]
for x in koordinates:
    print(x)

fields = [['#' for col in range(x_max - x_min + 1)] for row in range(y_max - y_min + 1)]
print('-----------------')

for v in koordinates:
	col, row = v
	fields[row][col] = '.'

fields.reverse()
for x in fields:
	print(x)

exit()





koordinates = [[x[0] * 2 + start[0], x[1] * 2 + start[1]] for x in koordinates]
koordinates = [start] + koordinates;
print(koordinates)



print(start)
print(data)
print(path)
print(fields)
print('-------')
koord_ = [koordinates[0]]

for x in zip(koordinates[:-1], koordinates[1:]):
	koord_ += [[int((x[0][0] + x[1][0]) / 2), int((x[0][1] + x[1][1]) / 2)], x[1]]
	fields[int((x[0][1] + x[1][1]) / 2)][int((x[0][0] + x[1][0]) / 2)] = '|'

for x in koord_:
	print(x)

for x in koordinates:
	fields[x[1]][x[0]] = ' '
fields[6][4] = 'S'
for x in fields:
	print(x)

"""
print("Result part 1: ", result_1)
print("Result part 2: ", result_2)
"""
