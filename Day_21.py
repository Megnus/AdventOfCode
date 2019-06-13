import _thread
import math
import time


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
	print("Starting thread: ", register)
	values = set()
	d = 0
	num = 0
	while register[ip] < max_lines:
		instruction = data[register[ip]]
		if register[ip] == 18:
			d = int(register[4] / 256)
			c = 1
			b = 25
			register[3] = d
			register[2] = c
			register[1] = b
		
		#print(register)
		if register[ip] == 28:
			values.add(register[5])
			if len(values) > num:
				print(len(values), register[5])
			num = len(values)
			# print(len(values), register[5], values, register[3], d, register[2], c)
			
		#print(register[ip], instruction, register)
		register = operation(register, instruction)
		register[ip] += 1
		# time.sleep(1)

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

initialization()
result_1 = execute([1, 0, 0, 0, 0, 0])
# 3941014


exit()


# Create two threads as follows
try:
	for i in range(0, 200):
		_thread.start_new_thread(execute, ([i, 0, 0, 0, 0, 0], ))
		time.sleep(1)
except:
	print("Error: unable to start thread")

while True:
	pass

# result_2 = execute([1, 0, 0, 0, 0, 0])
# print("Result part 1: ", result_1)
# print("Result part 2: ", result_2)
