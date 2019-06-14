def initialization():
	global data, ip, max_lines
	f = open('Input/input_day_21.txt', 'r')
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


def execute(register):
	initialization()
	reg_values = []
	while True:
		instruction = data[register[ip]]
		if register[ip] == 18:
			a, _, _, _, e, f = register
			register = [a, 25, 1, int(register[4] / 256), e, f]
		if register[ip] == 28:
			if register[5] in reg_values:
				return reg_values
			reg_values.append(register[5])
		register = operation(register, instruction)
		register[ip] += 1
	

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


values = execute([0, 0, 0, 0, 0, 0])
result_1, result_2 = values[0], values.pop()
print("Result part 1: ", result_1)
print("Result part 2: ", result_2)
