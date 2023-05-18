import re
str = "Acordei às 08:00, comi 12:30, dormi às 23:59!"
for m in re.finditer(r'(\d\d):(\d\d)',str):
    print(m.expand(r'\1 horas, \2 minutos'))