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
            checkpoint = (x + 2 * dx, y + 2 * dy)
            path.append([char, checkpoint])
            print(char, end=' ')
        elif char == '(':
            # path.append(char)
            index += explore(string[index:], checkpoint, ')')
        elif char == '|':
            # path.append(['R', checkpoint])

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

fields = [[' # ' for col in range(x_max - x_min + 1)] for row in range(y_max - y_min + 1)]
print('-----------------')

for v in koordinates:
    col, row = v
    if [col, row] == start:
        fields[row][col] = ' X '
    else:
        fields[row][col] = ' . '

distances = [[0 for col in range(x_max - x_min + 1)] for row in range(y_max - y_min + 1)]
# distances[-y_min][-x_min] = '1'


for col, row in koordinates:
    fields[row][col] = ' . '

# fields[-y_min][-x_min] = 'X'
fields.reverse()

for x in fields:
    print(x)

print()
ar = [(0, 1), (-1, 0), (1, 0), (0, -1)]

print()
tracks = []
tracks.append(start)
col, row = start
steps = 0
fields[row][col] = f"{steps:03d}"


while tracks:
    print(tracks)
    steps += 1
    positions = []
    for col, row in tracks:
        for v in ar:
            x, y = v
            try:
                if fields[row + y][col + x] == ' . ':
                    fields[row + y][col + x] = f"{steps:03d}"
                    positions.append([col + x, row + y])
            except IndexError:
                pass
    tracks = positions
    
for x in fields:
    print(x)
    
for row in fields:
    for el in row:
        try:
            print(int(el))
        except:
            pass

flat_list = max([int(item) for sublist in fields for item in sublist if item.isdigit()])
print(flat_list)

print(f"{1:03d}")
