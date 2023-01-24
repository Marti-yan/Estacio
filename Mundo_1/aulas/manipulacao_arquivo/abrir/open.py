import os

arq1 = open("dados1.txt")#caminho relativo
arq2 = open("C:/xampp\htdocs/aulas_php\Aulas_estacio\mundo1\Aulas_Python/aulas\manipulacao_arquivo/abrir\dados1.txt") # caminho absoluto relat

arq3 = open("documento/dados2.txt") # caminho relativo
arq4 = open("C:/xampp\htdocs/aulas_php\Aulas_estacio\mundo1\Aulas_Python/aulas\manipulacao_arquivo/abrir\documento\dados2.txt") # caminho absoluto


print(os.path.relpath(arq1.name))
print(os.path.abspath(arq1.name))
print(arq1)

print()

print(os.path.relpath(arq3.name))
print(os.path.abspath(arq3.name))
print(arq3)

print()

print(f"Nome do arquivo: {arq1.name}")
print(f"Modo do arquivo: {arq1.mode}")
print(f"Arquivo fechado: {arq1.closed}")
