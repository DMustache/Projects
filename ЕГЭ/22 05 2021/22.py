import re
from string import ascii_uppercase as as_up
with open(r'ЕГЭ\22 05 2021\fle.txt', mode='r', encoding='utf-8') as f:
    text = f.read()

print(max(re.findall('*'.join(as_up)+'*', text), key=len), re.findall('*'.join(as_up)+'*', text).count(len('ABBBBCCCCDDEF')))