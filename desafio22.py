'''
4-escreva um programa q receba uma palavra com mais de cinco letras
e troque as ultimas quatro letras pela palavra gato. ex: comida = cogato . 
'''

palavra = input('digite uma palavra: ')
contagem = len(palavra)

if contagem > 5:
	print('sua palavra: ')
	letra = palavra[0:2]
	resultado = letra
else:
	print('Sua palavra ñ foi add')