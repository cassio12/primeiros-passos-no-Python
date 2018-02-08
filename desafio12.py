# escreva um algoritimo q reseba a data de nascimento de um usuario, 
# e compare essa data com a data existente pŕe cadastrada. Se a senha for diferente
# exiba uma mensagem de erro e pergunte novamenta a senha



senha = input('Digite uma senha numerica: ')
data = input('Digite sua data de nascimento: ')

while senha != data:
	senha = input('Erro, sua senha não pode ser diferente a data de nascimento, digite uma senha diferente: ')
else:
	print('Sua senha foi aceita com sucesso')		
