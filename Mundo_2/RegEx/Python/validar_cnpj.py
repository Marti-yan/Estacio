import re

expr = re.compile('\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}')

cnpj = input("Digite um CNPJ: ")
if expr.search(cnpj):
    print("O CNPJ %s é valido" % (cnpj))
else:
        print("O CNPJ %s não é valido" % (cnpj))