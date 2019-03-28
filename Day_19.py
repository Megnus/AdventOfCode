def initialization():
	global data, ip, max_lines
	f = open('Input/input_day_19_test.txt', 'r')
	f = open('Input/input_day_19_seng.txt', 'r')
	f = open('Input/input_day_19.txt', 'r')
	in_data = f.read()
	f.close()
	lines = in_data.splitlines()
	ip_line = lines.pop(0)
	ip = int(ip_line.replace('#ip ', ''))
	data = [[a, int(b), int(c), int(d)] for a, b, c, d in [x.split(' ') for x in lines]]
	max_lines = len(lines)


def operation(r, operation):
	code, a, b, c = operation
	r[c] = operations[code](a, b, r)
	return r


def injection(reg):
	a, b, c, d, e, f = reg
	if d % e == 0:
		a += e
	b = d + 1
	f = 0
	return [a, b, c, d, e, f]


def execute(register):
	initialization()
	while register[ip] < max_lines:
		if register[ip] == 3:
			register = injection(register)
			register[ip] = 12
		instruction = data[register[ip]]
		register = operation(register, instruction)
		register[ip] += 1
	return register[0]


operations = {
	'addr': lambda a, b, r: r[a] + r[b],
	'addi': lambda a, b, r: r[a] + b,
	'mulr': lambda a, b, r: r[a] * r[b],
	'muli': lambda a, b, r: r[a] * b,
	'banr': lambda a, b, r: r[a] & r[b],
	'bani': lambda a, b, r: r[a] & b,
	'borr': lambda a, b, r: r[a] | r[b],
	'bori': lambda a, b, r: r[a] | b,
	'setr': lambda a, b, r: r[a],
	'seti': lambda a, b, r: a,
	'gtir': lambda a, b, r: 1 if a > r[b] else 0,
	'gtri': lambda a, b, r: 1 if r[a] > b else 0,
	'gtrr': lambda a, b, r: 1 if r[a] > r[b] else 0,
	'eqir': lambda a, b, r: 1 if a == r[b] else 0,
	'eqri': lambda a, b, r: 1 if r[a] == b else 0,
	'eqrr': lambda a, b, r: 1 if r[a] == r[b] else 0}


result_1 = execute([0, 0, 0, 0, 0, 0])
result_2 = execute([1, 0, 0, 0, 0, 0])
print("Result part 1: ", result_1)
print("Result part 2: ", result_2)
