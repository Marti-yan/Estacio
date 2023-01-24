import time

a = time.time() #Número de segundos passados desde o início da contagem (epoch). Por padrão, o início é 00:00:00 do dia 1 de janeiro de 1970.
print(a)

b = time.ctime(a) #Uma string representando o horário local, calculado a partir do número de segundos passado como parâmetro.
print(b)

c = time.gmtime(a) #Converte o número de segundos em um objeto struct_time descrito a seguir.
print(c)

d = time.localtime() #Semelhante à gmtime(), mas converte para o horário local.
print(d)

e = time.sleep(3) #A função suspende a execução por determinado número de segundos.
print("isso provavelmente so vai aparecer dps de 3 segundos")


print("///////////////////////////////////")
x=time.time()
print(f'Local time: {time.ctime(x)}')
y = time.gmtime(a)[0] 
print(y)