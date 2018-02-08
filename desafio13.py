#escreva um algoritimo para recarga de celular, que receba um numero de telefone 
#e comuperguntarmos novamente o numero para confirmar. se o numero estiver errado 
#peça para tentar novamente o numero para confirmar. se o numero estiver errado 
#peça para tentar novamente e exiba uma mensagem de erro, se ñ, mostre uma mensagem 
#informando q a transação foi feita. 

numero = input('Digite seu numero de telefone: ')
confirmação = input('Digite novamente para confirmar seu numero: ')

while numero != confirmação: 
	confirmação = input('Erro, o numero de confirmaçã esta diferente, digite novamente: ')
else:
	print('Sua transação foi feita com sucesse')	

	