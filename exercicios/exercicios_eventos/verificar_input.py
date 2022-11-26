
try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Entre com um número válido. ")


while True:
    try:
        x = int(input('Digite um Número: '))
        break
    except ValueError:
        print("Entre com um número válido. ")



def dividir(x,y):
   try:
       resultado = x/y
       print(f"A resposta é: {resultado}")
   except ZeroDivisionError:
       print("Divisão por zero")


dividir(3,2)
dividir(3,0)

try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")