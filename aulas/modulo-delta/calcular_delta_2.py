import math
import m1_delta

delta = 0

a = int(input("Entre com o coeficiente 'a' da equação: "))
b = int(input("Entre com o coeficiente 'b' da equação: "))
c = int(input("Entre com o coeficiente 'c' da equação: "))

delta = m1_delta.calcular(a,b,c)
print(f"O valor de delta é: {delta}")

if delta == 0:
    print("A equação tem 1 raiz real")
    raiz = (-b + math.sqrt(delta))/2*a
    print(f"A raize é {raiz}")
elif delta > 0:
    print("A equação tem 2 raizes reais")
    raiz1 = (-b + math.sqrt(delta))/2*a
    raiz2 = (-b - math.sqrt(delta))/2*a
    print(f"As raizes são {raiz1} e {raiz2}")
else:
    print("A equação não tem uma raiz real")