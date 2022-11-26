def function1():
    global a
    a = 10
    print("O valor da variavel dentro  da função é: {}".format(a)) #variavel local
    #print("O valor da variavel dentro  da função é:", a)


a = 30
function1()
print("A variavel global é: {}".format(a))









