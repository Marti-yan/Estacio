lista = [1, 2, 3, 4, 5,6,7,8]
 
def impar(item):
    return item % 2 != 0

def main():
    nova_lista = filter(impar, lista)
    print(list(nova_lista))
 
if __name__ == "__main__":
    main()
    
print("---------------------  ")
    
# com lambda
verificar = lambda x: x % 2 == 0
print(f'Teste de paridade (5): {verificar(5)}')
pares = list(filter(verificar,lista))
print(f'Pares: {pares}')
    
    
    