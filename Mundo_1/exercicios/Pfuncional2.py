Lnumeros = [9.56783, 7.57568 , 3.00914, 6.2321]
Lprecisao = [2,2,3,3]

arredondar = lambda x,y: round(x,y)

resultado = list(map(arredondar,Lnumeros,Lprecisao))

print(resultado)