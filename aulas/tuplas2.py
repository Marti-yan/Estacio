#tuplas não podem ser alteradas

tuplax = (1, 'Hello', [1, 2], (3,4))
print(tuplax)

tupla = ('a', 'b', 'c')
item = tupla[2]
print(item)

indice_a = tupla.index('a')
print(indice_a)

tupla = ('a', 'b', [1, 2, 3], (4, 5, 6))
for elemento in tupla:
    #print(elemento)        # até aqui vai mostra cada index = []() contam como um unico index
    for i in elemento:
        print(i)            # aqui ja vai mostrar cada elemento, até quais estão no []()

import collections
pessoa = collections.namedtuple('pessoa','idade nome')
joao = pessoa(nome='joao',idade=18)
print(joao)
print(joao.nome)
print(joao.idade)

