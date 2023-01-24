veiculos = ['aviao','carro','moto','navio']
p_maiscula = lambda x: str.upper(x)
nomes_maisculos = list(map(p_maiscula, veiculos))
print(f'Os nomes em maisculos é: {nomes_maisculos}')