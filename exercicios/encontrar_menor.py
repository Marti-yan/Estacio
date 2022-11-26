def encontrar_minimo(lista):
    minimo = lista[0]
    for i in lista:
        if(i<minimo):
            minimo = i
    return minimo



lista_teste = [10,0.9,3,1,5,4]
menor = encontrar_minimo(lista_teste)
print(f"O menor elemento da lista foi: {menor}")