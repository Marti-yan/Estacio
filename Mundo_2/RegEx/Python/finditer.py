import re

str = "Acordei às 08:00, comi 12:30, dormi às 23:59!"
for m in re.finditer(r'(\d\d):(\d\d)', str):
    hora = m.group(1)
    min = m.group(2)
    print("%s horas, %s minutos."%(hora, min))