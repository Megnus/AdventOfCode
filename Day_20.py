import re


def initialization():
	f = open('Input/input_day_20.txt', 'r')
	in_data = f.read()
	f.close()
	print(in_data)
	re_before = re.sub('\(.+?\)', '', 'EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)')
	re_before = re.sub('^[A-Z]', '', 'EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)')
	re_before = re.findall('[A-Z]+', in_data)
	print(re_before)
	re_before = re.findall('[\(|\)|\|]', in_data)
	print(re_before)
	re_before = re.findall('\(.+?\)', 'EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)')
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
	return re.findall('(?<=\^).+(?=\$)', in_data)[0]


data = initialization()
data = list(data)
map = {'E': (1, 0), 'W': (-1, 0), 'N': (0, 1), 'S': (0, -1), '|': '|', '(': '(', ')': ')'}
data = [map[x] for x in data] # if x not in '(|)']

matrix = []
m = (0, 0)
for p in data:
	if type(p) is str:
		continue
	x, y = p
	matrix.append(m)
	mx, my = m
	m = (mx - x, my - y)
print(matrix)











"""
print("Result part 1: ", result_1)
print("Result part 2: ", result_2)
"""
