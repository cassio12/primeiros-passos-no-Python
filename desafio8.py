usuario = input('digite o usuario: ')
senha = input('digite uma senha: ')
mascote = input('digite o nome do mascote: ')
nascimento = input('digite a data de nascimento: ')
letras = len(senha) 

if senha == usuario or senha == mascote or senha == nascimento: 
	print('desiste da vida')
elif letras < 6:
	print('a senha tem menos de 6 digitos')
else:
	print('')