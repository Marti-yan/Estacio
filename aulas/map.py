lista = [1, 2, 3, 4, 5]

def triplica(item):
    return item * 3

def main():
    nova_lista = map(triplica, lista)
    print(list(nova_lista))

if __name__ == "__main__":
    main()


#//////////////////////////////////////////////////////


lista2 = [1, 2, 3, 4, 5]
nova_lista2 = map(lambda item: item * 3, lista)# função lambda

def main2():
    print(list(nova_lista2))

if __name__ == "__main__":
    main2()