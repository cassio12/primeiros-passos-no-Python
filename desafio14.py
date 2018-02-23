# crie um programa q sorteie um valor entre 1 e 20.

# crie um programa q sortei um valor entre 1 e 30 e receba um valor do usuario se o usuario
# acertar o valor exiba uma mensegem.

# crie um programa q sorteia um valor entre 1 e 30 e receba
# um valor do usuario. verifique se ele acertou, dê a ele 3 chances de tentar.  
# 
# 

import random

number = random.randint(1,20)	
	
numero_de_tentativas = 0

while numero_de_tentativas < 2:
 	tentativa = int(input('escreva um numero '))
 	numero_de_tentativa = numero_de_tentativas + 1
if tentativa == number:
 	print('vc acertou' + srt(numero_de_tentativas) + ' vezes')
else:
	print('vc errou. o numro é ' + number)