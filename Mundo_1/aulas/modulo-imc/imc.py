print("Módulo IMC importado")

def calcular_imc(peso, altura):
    print("parâmetro peso: ", peso)
    print("parâmetro altura: ", altura)
    global imc
    imc = peso / altura**2
    print("IMC: ", imc)
    return imc

# def teste():
#     print("função de teste")
    
def classificar_indice():
    if imc < 18.5:
        print("baixo peso")
    elif imc <25:
        print("no peso")
    elif imc < 30:
        print("sobre peso")
    else:
        print("obeso")
    
    
    







