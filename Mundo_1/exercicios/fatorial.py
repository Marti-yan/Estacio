#jeito 1
def fatorial_iterativo(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

#jeito 2
def fatorial_recursivo(n):
    if((n==0)or(n==1)):
        return 1
    return n*fatorial_recursivo(n-1)


numero = eval(input("Digite um numero: "))
print(f'O fatorial de {numero} é: {fatorial_iterativo(numero)}')
print(f'O fatorial de {numero} é: {fatorial_recursivo(numero)}')