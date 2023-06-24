import re

def text_match(text):
    patterns = r'ab?'
    if re.search(patterns, text):
        return 'Deu Match'
    else:
        return 'erro'
    
    
print(text_match('ab'))
print(text_match('acbbc'))
print(text_match('a'))
print(text_match('abbc'))
print(text_match('aabbc'))