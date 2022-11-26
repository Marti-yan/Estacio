lista = [10, 2, 5, 7, 6, 3]
soma = 0

n=len(lista)
for i in range(n):
    if( lista[i] % 2 == 0):
        soma = soma+lista[i]
print(f'A soma dos elementos pares da lista é : {soma}')


soma = 0
for num in lista:
    if(num%2==0):
        soma=soma+num
print(f'A soma dos elementos pares da lista é : {soma}')