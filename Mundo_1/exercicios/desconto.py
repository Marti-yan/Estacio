qtde = eval(input("Quantos itens foram comprados?: "))
valor = 10.00
if (qtde > 10 and qtde <=20):
    subtotal = valor * qtde
    print(f'SubTotal: {subtotal}')
    total = subtotal * 0.9
    print(f'Total: {total}')
elif (qtde > 20):
    subtotal = valor * qtde
    print(f'SubTotal: {subtotal}')
    total = subtotal * 0.8
    print(f'Total: {total}')
else:
    subtotal = valor * qtde
    print(f'SubTotal: {subtotal}')
    print(f'Total: {subtotal}')



