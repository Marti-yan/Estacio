arquivo = open("dados.txt","r")

conteudo = arquivo.read()
print("Todo o conteudo do arquivo")
print(repr(conteudo), '\n')

releitura = arquivo.read()
print("Releitura de todo o conteudo do arquivo")
print(repr(releitura), '\n')

arquivo.close()


arquivo_reaberto = open("dados.txt","r")

conteudo_reaberto = arquivo_reaberto.read()
print("Todo o conteudo do arquivo ")
print(repr(conteudo_reaberto))

print()

arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print("Todo o conteudo do arquivo após o SEEK")
print(repr(conteudo_seek))

arquivo.close()





