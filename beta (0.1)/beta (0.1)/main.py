from deco import logo
import functions as func

logo()

query = [['Математика', 'математика', 'матем'], ['Камень, ножницы, бумага', 'камень ножницы бумага', 'Камень ножницы бумага']]

while True:
	ask = input('Гость: ')
	if (ask == query[0][0]):
		func.calc()
	elif (ask == query[0][1]):
		func.calc()
	elif (ask == query[0][2]):
		func.calc()
	elif (ask == query[1][0]):
		func.rsp()
	elif (ask == query[1][1]):
		func.rsp()
	elif (ask == query[1][2]):
		func.rsp()
	else:
		print('Nikirina: Не поддерживается!');

