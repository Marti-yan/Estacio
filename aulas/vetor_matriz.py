from numpy import array
notas_real = array([2,5,10,20,50,100,300], dtype=int)
print(notas_real)
print(notas_real[5])
print(notas_real[4]+notas_real[5])
print()

indice = int(input("Digite o valor do indice: "))
element = int(input("Digite o valor do elemento: "))
notas_real[indice] = element
print(f"Novo vetor: {notas_real}")

for i in range(len(notas_real)): # mostra os indices do vetor
    print(f" for 1: {i}")
    
    
for element in notas_real: #mostra oq esta dentro do vetor
    print(f"for 2: {element}")

cadeiras = array([["Português","Matemática","Química"], ["História", "Geografia", "Física"]], dtype=str)
print("primeria linha")
print(cadeiras[0][0],cadeiras[0][1],cadeiras[0][2])
print()
print("segunda linha")
print(cadeiras[1][0],cadeiras[1][1],cadeiras[1][2])

cadeiras[1][2] = "calculo"
cadeiras[0][1] = "algebra"

print()
print("/////////        Grade nova         ///////////")
print("primeria linha")
print(cadeiras[0][0],cadeiras[0][1],cadeiras[0][2])
print()
print("segunda linha")
print(cadeiras[1][0],cadeiras[1][1],cadeiras[1][2])

for linha in cadeiras:
    print("\nnova linha: \n")
    for elemento in linha:
        print(elemento)