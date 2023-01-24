arquivo = open("dados.txt","r")

conteudo = arquivo.readlines()

print("Tipo do conteudo: ",type(conteudo))

print("Conteudo retornado pelo readlines:")
print(repr(conteudo))

arquivo.close()
