import re

texto = '''Método, descrição
teste(),Testa valores
split(),Separa strings''' #''' são usados para declarar string com quebra de linha
items = re.split(r'[\n]', texto); #divide o texto em linhas, \n quebra de linha
print(items)

for index, item in enumerate(items, start=0):   # intera a lista, padrão do index é zero
  #print(index, item)
  listaLinha = re.split(r'[/,]', item);
  for indexLinha, linha in enumerate(listaLinha, start=0):   # padrão é zero
    print('-'+linha)
  print('-------------')

# ['Método,descrição', 'teste(),Testa valores', 'split(),Separa strings']
# -Método
# -descrição
# -------------
# -teste()
# -Testa valores
# -------------
# -split()
# -Separa strings
# ------------- 