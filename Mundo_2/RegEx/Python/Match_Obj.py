import re

string = 'De grão em grão, a galinha enche o papo'
m = re.search(r'g[A-z]l[A-z]+', string)
if m:
    print(m)
    print(m.group())  # galinha
    print(m.start())  # 19
    print(m.end())    # 26
    print(m.span())   # (19, 26)
    
    
print('\n')

m2 = re.search(r'(..)/(..)/(....)','05/06/2022')
if m2:
 print(m2)
 print(m2.group(0))  # 05/06/2022
 print(m2.group(1))  # 05
 print(m2.group(2))  # 06
 print(m2.group(3))  # 2022
 print(m2.span(0))   # (0, 10) 
 print(m2.span(1))   # (0, 2)
 print(m2.span(2))   # (3, 5)
 print(m2.span(3))   # (6, 10)
 print(m2.groups())  # ('05', '06', '2022')