peso = eval(input('Digite seu peso: '))
altura = eval(input('Informe sua altura em M: '))
imc = peso/altura**2
print(f'O seu IMC é de {imc}')
print('O seu imc é de {:8.3}'.format(imc))
# print('O seu imc é de {:8.3}'.format(imc*10000))


