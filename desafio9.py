numero1 = input('digite um numero de 0 a 9: ')
numero2 = input('digite um numero de 0 a 9: ')
numero3 = input('digite um numero de 0 a 9: ')

if numero1 > numero2 > numero3 :
	print('o numero ' + numero1 + ' é maior')
elif numero2 > numero1 > numero3 :
	print('o numero ' + numero2 + ' é maior')
elif numero3 > numero2 > numero1 :
	print('o numero ' + numero3 + ' é maior')	
else:
	print('todos são iquais ')	