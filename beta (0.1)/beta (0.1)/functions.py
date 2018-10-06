import math
from deco import calcbegin, rspbegin, div

def calc():
	calcbegin()
	num = int(input('Первое число: '))
	num_2 = int(input('Второе число: '))
	opera = input('Операция: ')

	if (opera == 'help'):
		print('+ (прибавление)')
		print('- (отнимание)')
		print('x (умножение)')
		print('/ (деление)')
		print('% (деление по модулю)')
		print('m (степень)')
		print('sqrt (корень)')
		print('sin (синус)')
		print('cos (косинус)')
	elif (opera == '+'):
		res = num + num_2
		print(res)
	elif (opera == '-'):
		res = num - num_2
		print(res)
	elif (opera == 'x'):
		res = num * num_2
		print(res) 
	elif (opera == '/'):
		res = num / num_2
		print(res)
	elif (opera == '%'):
		res = num % num_2
		print(res)
	elif (opera == 'm'):
		res = num ** num_2
		print(res)
	elif (opera == 'sqrt'):
		res = num // num_2
		print(res)
	elif (opera == 'sin'):
		result = num + num_2
		res = math.sin(result)
		print(res)
	elif (opera == 'cos'):
		result = num + num_2
		res = math.cos(result)
		print(res)
	else:
		print('Нет операции!')
	div()

def rsp():
	rspbegin()
	step = input('Ваш ход: ')
	if (step == 'Камень'):
		print('Nikirina: Бумага')
	elif (step == 'Ножницы'):
		print('Nikirina: Камень')
	elif (step == 'Бумага'):
		print('Nikirina: Ножницы')
	div()