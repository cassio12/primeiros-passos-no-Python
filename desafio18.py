'''
Maria tem q tomar remedio de 15 em 15 minutos, escreva um programa que 
mostre todos os horarios em que Maria precisa tomar um remedio num periodo
de um dia.
'''

for hora in range(0,24):
	for minuto in range(0,60,15):
	print(str(hora)+ ':' + str(minutos))

