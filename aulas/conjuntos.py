conjunto = {'a', 1, 2020, (28, 12), 'a'}   #  ← itens duplicados são automaticamente removidos
for elemento in conjunto:
    print(elemento)

conjunto1 = set()
conjunto1.add(1)
conjunto1.add(2)
print(conjunto1)
conjunto1.add(2)   #  ← por já conter itens duplicados, a inserção é ignorada
conjunto1.add(3)
conjunto1.add(4)
print(conjunto1)
conjunto1.discard(1)
conjunto1.remove(2)
print(conjunto1)
conjunto1.clear()
print(conjunto1)

conjunto2 = {'a', 1, 2, 3}
print(conjunto2.pop())  # remove de forma aleatoria

conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_b = {3, 4, 5}   # passa a valer essa que foi dps
uniao = conjunto_a.union(conjunto_b)  # junta a+b (sem os numeros repitidos)
print(uniao)
intersecao = conjunto_a.intersection(conjunto_b)    # o numero em comum entre a+b
print(intersecao)       
diferenca = conjunto_a.difference(conjunto_b)  # oq tem no conjuto a q não tem no b
print(diferenca)

conjunto1 = {100, 200, 300}
conjunto2 = {200, 400, 500}
print(conjunto1.difference(conjunto2))






