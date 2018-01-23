funsionario =input('nome do funsionario? ')
horasTrabalho = int(input('quantas horas o funsionario trabalha? '))
valorRecebidoH = int(input('valor que o funcionario recebe por hora? '))

total =horasTrabalho * valorRecebidoH

print(total)

print('o funcionario ' + funsionario + 'trabalhou' + str(horasTrabalho) + 'horas.\nvalor resebido por hora ' + str(valorRecebidoH) + 'o funcionario recebe ' + str(total))