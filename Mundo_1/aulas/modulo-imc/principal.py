#from imc import *  # assim eu não preciso escrever o 'imc.' e posso colocar o nome e importar apenas a função desejada

from imc import calcular_imc
from imc import classificar_indice

#import imc  #assim eu tenho que colocar o 'imc.' antes das funções

print()
print("Inicio do programa")
print()

calcular_imc(altura=1.88,peso=98.1)
classificar_indice()

print()
print("Fim do programa")
# teste()