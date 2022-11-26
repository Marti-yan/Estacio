lista = ['a', 'b', 'c', 'b']
indice_c = lista.index('c')
print(indice_c)
print(lista.index('b'))

lista2 = ['avião', 'helicóptero', 'carro', 'navio']
print(lista2)
indice_carro = lista2.index('carro')
lista2[indice_carro] = 'moto'
print(lista2)

for i in lista2:
    print(i)

for i in range(0, len(lista2)):
    print(lista2[i])

lista = list()
lista.append('carro')
print(lista)

lista.append('moto')
lista.append('avião')
print(lista)

lista.insert(1, 'bicicleta')     # Inserimos o elemento bicicleta na posição de índice 1
print(lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_a.append(lista_b)
print(lista_a)

lista_a = [1,2,3]
lista_a.extend(lista_b)
print(lista_a)

lista_a.remove(4)
print(lista_a)
lista_a.clear()
print(lista_a)

lista = [3,2,1,6,9,10,59,4,100]
lista.sort()
print(lista)
lista.reverse()
print(lista)

print()
print(len(lista))
print(min(lista))
print(max(lista))
print(sum(lista))
media = sum(lista)/len(lista)
print(media)
print(f"{media:,.2f}")

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [4, 5, 6]
print(lista1 == lista2)
print(lista1 == lista3)
if 5 in lista3:
    print('Achei o 5!!!')
nova_lista = lista1 + lista3
print(nova_lista)
lista_repetida = lista1 * 3
print(lista_repetida)

lista = [1, 2, 3]
nova_lista = [item*5 for item in lista] #multiplica cada item da lista pelo numero
print(nova_lista)

lista2 = [0, 1, 2, 3, 4, 5, 6]
print(lista2)
nova_lista2 = [item for item in lista2 if item%2 == 0]
print(nova_lista2)

import copy


lista1 = [[1,2,3], [4, 5, 6],[7,8,9]]
lista2 = lista1  # as listas ficam totalmentes compartilhadas, se eu editar uma edita a outra

lista1.append([10,10,10])
lista2[2][2]=11

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")


print()


lista3 = [[1,2,3], [4, 5, 6],[7,8,9]]
lista4 = copy.copy(lista3) #o pedaço copiado vira uma lista compartilhada

lista3.append([10,10,10])
lista4[2][2] = 11

print(f"Lista 3: {lista3}")
print(f"Lista 4: {lista4}")


print()


lista5 = [[1,2,3], [4, 5, 6],[7,8,9]]
lista6 = copy.deepcopy(lista5) # cria uma lista (copia da que foi passada) totalmente idependente

lista5.append([10,10,10])
lista6[2][2] = 11

print(f"Lista 5: {lista5}")
print(f"Lista 6: {lista6}")


# ////////////////////////////////

lista = []
c = 1
x = int(input("Quantos valores vai ter seu conjunto: "))
while c <= x:
    i = input(f"valor {c} da lista: ")
    lista.append(i)
    c+=1
print(lista)   

