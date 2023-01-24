
#//////////////////////////////////////////////////////////////////

palavra = input('Entre com uma palavra: \n ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')

#//////////////////////////////////////////////////////////////////

n = 0
while n <= 10:
    print(n)
    n+=1

#//////////////////////////////////////////////////////////////////

while True:
    palavra = input('Entre com uma palavra: \n')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço')

#//////////////////////////////////////////////////////////////////

while True:
    print('Você está no primeiro laço.')
    opcao1 = input("Deseja sair dele? Digite 'SIM'' para isso. \n")
    if opcao1 == 'sim':
        break
    else:
        while True:
            print('Você esta no segundo laço.')
            opcao2 = input("Deseja sair dele? Digite 'SIM' para isso. \n")
            if opcao2 == 'sim':
                break
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')

#//////////////////////////////////////////////////////////////////

for num in range(1,11):
    if num == 5:
        continue
    else:
        print(num)
print('laço encerrado')

#//////////////////////////////////////////////////////////////////

for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')
