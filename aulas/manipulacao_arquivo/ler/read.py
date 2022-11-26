arquivo = open("dados.txt","r")

conteudo = arquivo.read()

print("Tipo do conteudo: ",type(conteudo))

print("Conteudo retornado pelo read:")
print(repr(conteudo))

arquivo.close()






