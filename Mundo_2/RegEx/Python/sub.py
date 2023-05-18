import re

texto= "08:00"
print(re.sub(r'\w', '.', 'Python'))     # ......
print(re.sub(r'\w', '.','Python', 2))   # ..thon
texto= "Quem viver verá"
print(re.sub(r'v\w', '#', texto))       # Quem ##r #rá



def data_por_extenso(m):
 dia = m.group(1)
 mes = m.group(2)
 ano = m.group(3)
 meses = {
   '01':'Janeiro', '02':'Fevereiro', '03':'Março',
   '04':'Abril',   '05':'Maio',      '06':'Junho',
  '07':'Julho',   '08':'Agosto',    '09':'Setembro',
  '10':'Outubro', '11':'Novembro',  '12':'Dezembro'
  }
 return dia + " de " + meses[mes] + " de " + ano
texto= "Hoje é dia 05/05/2022."
regex = r'(\d\d)/(\d\d)/(\d\d\d\d)'
print(re.sub(regex, data_por_extenso, texto))

# Hoje é dia 05 de Maio de 2022.