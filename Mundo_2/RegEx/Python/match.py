import re

str = "frase que será analisada pelo regex";
result = re.match(r'frase', str)
print(result)  # <_sre.SRE_Match object; span=(0, 5), match='frase'>
result = re.match("frase", str)
print(result)  # <_sre.SRE_Match object; span=(0, 5), match='frase'>
result = re.match(r'analisada', str)
print(result)  # None
result = re.match(r'legal', str)
print(result)  # None



