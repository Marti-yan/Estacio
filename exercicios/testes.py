
# def foo(a):
#    return a + a + a
# b = 1
# foo(b)
# foo(b)
# foo(b)
# print(b)


# lista = ["cachorro","hamster",["pato","galinha","porco"],"gato"]
# print(lista[3][2])

# print((True + 2)**2)
# minha_lista = [ 0.5*item for item in [0, 1, 2, 3] ]
# print(minha_lista)

# lista = [5, 10, 20]
# soma = sum(lista)
# print(soma)
# assert soma == 35, "Aguardando sucesso!"
# assert soma !=35, "Aguardando erro!"

lista = [0, 2, 4, 6, 7, 8, 9]
for numero in lista: 
    assert numero % 2 == 0, "Número ímpar encontrado! ->" + str(numero)
    