from natsort import natsort_keygen
natsort_key = natsort_keygen()

def subC(numeros):
    return subC_recursivo([], sorted(numeros))

def subC_recursivo(atual,conjunto):
    if conjunto:
        return subC_recursivo(atual,conjunto[1:]) + subC_recursivo(atual + [conjunto[0]], conjunto[1:])
    return [atual]



numeros = []
c = 1
x = int(input("Quantos valores vai ter seu conjunto: "))
while c <= x:
    i = input(f"valor {c} da lista: ")
    numeros.append(i)
    c+=1
print(f"Conjunto: {numeros}")   



resultado = subC(numeros)
resultado.sort(key=natsort_key)
resultado1 = sorted(resultado, key=len)
print("SubConjuntos: ",resultado1)


