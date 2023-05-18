import re

string = 'De médico e Louco, todo mundo tem um pouco'
m = re.findall(r'[A-z]ou[A-z]+', string);
print(m)   			  # ['Louco', 'pouco'] 

texto="Corri 3km em 15 minutos, ouvindo CPM 22."
print(re.findall(r'\d+', texto))  # ['3', '15', '22']
print(re.findall(r'XXX', texto))  # []

texto= "Hora de acordar 06:00, trabalhar 08:30, almoçar 12:10, lanchar 16:15 e jantar 19:20."
print(re.findall(r'(\d\d):(\d\d)', texto))   # [('06', '00'), ('08', '30'), ('12', '10'), ('16', '15'), ('19', '20')]