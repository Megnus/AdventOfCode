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
			print(char, end=' ')
		elif char == '(':
			path.append(char)
			index += explore(string[index:], checkpoint, ')')
		elif char == '|':
			checkpoint = start
			path.append(char)
		elif char == end_char:
			path.append(char)
			return index
	return 0
		
	#return matrix


data = initialization()
#data = [map[x] for x in data] # if x not in '(|)']
end_char = '$'
print(list(data))
explore(list(data), (0, 0), end_char)
print(data)
print(path)


"""
print("Result part 1: ", result_1)
print("Result part 2: ", result_2)
"""
