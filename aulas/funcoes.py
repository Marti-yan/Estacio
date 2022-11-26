
# ////////////////////////////////////////////////////////////

def multiplicador(numero):
    a = 2  # esta variável tem escopo local
    print(f"Dentro da função, a variável vale: {a}")
    return a * numero

a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {a}")

# ////////////////////////////////////////////////////////////

def multiplicador(numero):
    return a * numero

a = 3  # esta variável tem escopo global
b = multiplicador(10)
print(f"A variável b vale: {b}")

# ////////////////////////////////////////////////////////////

def multiplicador(numero):
    global a  # todas as referências à variável a são para a global
    a = 2  # a global será alterado
    print(f"Dentro da função,  variável  vale: {a}")
    return a * numero

a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")


# ///////////////////////////////////////////////////////////

texto = "Qualquer Coisa Aqui"
print(texto)
print(texto.upper())
print(texto.lower())
print(texto.split())

# ///////////////////////////////////////////////////////////

a = ['U'] + ['RN']
print(a)
print(f"o tamanho da lista a é: {len(a)}")

# ///////////////////////////////////////////////////////////

deck = ['pikachu']
def inserir_novo():
    novo = input('Qual o nome do pokemon: ')
    if verificar(novo):
        deck.append(novo)
        mostrar_deck()
    else:
        print("esse card ja existe no deck")

def mostrar_deck():
    print(len(deck))
    print(deck)

def verificar(pokemon):
    if (pokemon in deck):
        return  False
    else:
        return True
inserir_novo()

# ///////////////////////////////////////////////////////////

def regressiva(x):
    if x<= 0 or x>=100:
        print("acabou")
    else:
        print(x)
        regressiva(x - 1)

x = 10
regressiva(x)

# ///////////////////////////////////////////////////////////

def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
        print(n)
        return n*fatorial(n-1)
        
     
fatorial(5)     

# ///////////////////////////////////////////////////////////

# /////////     FIBONACCI   /////////////////
#Determina o n-ésimo termo da  sequência de Fibonacci
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo))
