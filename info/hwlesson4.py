
# #1 
import re
text = input()
print(f'новая строчка:{text.replace('н', '!')}, кол-во символов:{len(max(re.findall(r'н+', text)))}')

# #2 но чеснто я просто хотела разобраться с регулярными выражениями
import re
text = input()
print(re.findall(r'\((.+?)\)', text))

#2 я вспомнила что вообще-то есть команда find в "ванильном" петоне

text = input()
print(text[text.find('(') + 1:text.find(')')])

#3
import re
text = input().lower()
print(re.findall(r'\bа\w+я\b', text))