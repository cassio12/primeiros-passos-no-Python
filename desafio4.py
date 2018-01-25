idade = int(input('coloque os dias desejados: '))

ano = idade / 365
dia =(idade % 365) / 30 
mes = (idade % 365) % 30

print( '%.0f ano(s)' % ano)
print( '%.0f dia(s)' % dia)
print( '%.0f mes(es)'% mes)