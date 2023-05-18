import re

string = 'Teste regex Python'
m = re.search(r'Py', string) 
if m:
  print('Casou')  # Casou
else:
  print('Não Casou')
print(m)  # <_sre.SRE_Match object; span=(12, 14), match='Py'>


# Lembre-se de que a função search( ) retorna apenas a primeira ocorrência.

string = 'Teste Python regex Python'
m = re.search(r'Py', string);
print(m)  # <_sre.SRE_Match object; span=(6, 8), match='Py'>