def ehpar(n):
    r = (n%2==0)
    return r

def somar_par(lst):
    soma=0
    for num in lst:
        if(ehpar(num)):
            soma += num
    return soma


lista = [10,2,3,1,5,4]
soma = somar_par(lista)
print(soma)

