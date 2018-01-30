idade = int(input('descubra se vc pode votar, em que ano você nasceu ? ' ))
nome = input('qual o seu nome ? ')

if idade < 1999:
	print('parabéns ' + nome + ' você é maior já pode votar obrigatoriamente. ')
elif idade < 2002:
	print('parabéns ' + nome + ' você pode votar por opção. ')	
else:	
	print('lamento ' + nome + ' você é menor ainda ñ pode votar. ')



# crie um programa que receba a 
# idade de uma pessoa e verifique se 
# ela pode votar 
#
# entrada: ola Dalianny
# sida: dalianny tem 21 anos e pode votar 
