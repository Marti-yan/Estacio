
def func():
    x = 1
    print(x)
x = 10
func()
print(x)

print( 2 + 3 - 4 ** 2 + 5 / 2 - 5 // 2)

a = ['U'] + ['RN']
print(len(a))
b = ['4'] * 4
print(len(b))


a = ['10']
b = ['20']
c = ['30']

print (a+b+c)
print(a*2+b*3+c*4)

#f(x) = ax+b
# x = -b/a com 'a' diferente de zero
a=10
b=50
x=-b/a
print(f'A raiz da equação do primeiro grau é: x={x}')


idade = int(input('Informe a idade da criança: \n'))
if idade < 5:
    print('A criança deve ser vacinada contra a gripe.')
    print('Procure o posto de saúde mais próximo.')
elif idade == 5:
    print('A vacina estará disponível em breve.')
    print('Aguarde as próximas informações.')
else:
    print('A vacinação só ocorrerá daqui a 3 meses.')
    print('Informe-se novamente neste prazo.')
print('Cuide da saúde sempre. Até a próxima.')

s = 0
for i in range(5):
    s += 3 * i
print(s)

s = 0
a = 1
while s < 5:
      s = 3*a
      a += 1
      print(s)

escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s)

def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia *
    km_rodado) * multiplicador
    return valor


pagamento = taximetro(3.5)
print(pagamento)


def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')

def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1()
func2()
print(f'Programa principal - x = {x}')


def taximetro(distancia):
    def calculamult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculamult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

dist = int(input("qual foi a distancia percorrida?: "))
pagamento = taximetro(dist)
print(f'O valor a ser pago é: R${pagamento}')


def func1(x):
     x = 10
     print(x)


x = 0
print(x)
func1(x)
print(x)

def rec(n):
     if n < 2:
          return rec(n - 1)


print(rec(1))
