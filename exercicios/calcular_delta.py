def calcular(coef1,coef2,coef3):
    global delta
    # //delta da eq de 2 grau = b**2 - 4.a.c\\
    delta = coef2*coef2 - 4*coef1*coef3
    #return delta

delta = 0

a = int(input("Entre com o coeficiente 'a' da equação: "))
b = int(input("Entre com o coeficiente 'b' da equação: "))
c = int(input("Entre com o coeficiente 'c' da equação: "))

calcular(a,b,c)
print(f"O valor de delta é: {delta}")

if delta == 0:
    print("A equação tem 1 raiz real")
elif delta > 0:
    print("A equação tem 2 raizes reais")
else:
    print("A equação não tem uma raiz real")