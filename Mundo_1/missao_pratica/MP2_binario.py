x = int(input("Digite um numero decimal: "))
bin=''
while x>0:
    bin+= str(x%2)
    x//=2

print(f"O numero em Binario é: {bin[::-1]}")


