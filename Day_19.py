#from typing import Dict, Any, Union


def initialization():
	global data, ip, max_lines
	f = open('Input/input_day_19.txt', 'r')
	f = open('Input/input_day_19_test.txt', 'r')
	f = open('Input/input_day_19_seng.txt', 'r')
	in_data = f.read()
	f.close()
	lines = in_data.splitlines()
	ip_line = lines.pop(0)
	ip = int(ip_line.replace('#ip ', ''))
	data = [[a, int(b), int(c), int(d)] for a, b, c, d in [x.split(' ') for x in lines]]
	max_lines = len(lines)


def operation(r, operation):
	code, a, b, c = operation

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
	
	r[c] = operations[code](a, b, r)
	#r[3] = 0
	return r


def counter_step(register):
	global ip
	ip = register[5]
	ip += 1
	register[5] = ip
	return register


initialization()
print(ip, data)
#exit()
register = [0, 0, 0, 0, 0, 0]
ip = 0
while register[0] < max_lines:
#for i in range(0, 20):
	instruction = data[register[5]]
	# if ip >= max_lines:
	# 	break
	#print(register, instruction, end='', flush=True)
	register = operation(register, instruction)
	#print(register)
	register[5] += 1
	#register = counter_step(register)
print(max_lines)
print(register)

