##############################################
"""text = 'salam ali call Kuubi? k g r emroz e d shanbe ast'
text = text.split()
t2 = ''
for i in text:
    t2 += i[0]
del text
passU = (('a', '@'), ('i', '1'), ('o', '0'), ('s', '*'), ('c', '('), ('v', '&'))
for i in passU:
    t2 = t2.replace(i[0], i[1])
t2 = t2.lower()
t2 = list(t2)
for t in range(0, len(t2), 2):
    t2[t] = t2[t].upper()
t2 = ''.join(t2)
print(t2)
"""
############################################
'''from colorama import Fore

dic_cool = {
    'BLACK+': Fore.LIGHTBLACK_EX,
    'RED+': Fore.LIGHTRED_EX,
    'GREEN+': Fore.LIGHTGREEN_EX,
    'YELLOW+': Fore.LIGHTYELLOW_EX,
    'BLUE+': Fore.LIGHTBLUE_EX,
    'MAGENTA+': Fore.LIGHTMAGENTA_EX,
    'CYAN+': Fore.LIGHTCYAN_EX,
    'WHITE+': Fore.LIGHTWHITE_EX,
    'BLACK': Fore.BLACK,
    'RED': Fore.RED,
    'GREEN': Fore.GREEN,
    'YELLOW': Fore.YELLOW,
    'BLUE': Fore.BLUE,
    'MAGENTA': Fore.MAGENTA,
    'CYAN': Fore.CYAN,
    'WHITE': Fore.WHITE,
    'RESET': Fore.RESET,
}
txt = input(Fore.LIGHTRED_EX + 'enter color name :  ')
if txt.upper() in dic_cool:
    print(dic_cool[txt.upper()] + txt)'''
############################################
"""import re

text = 'https://backendbaz.ir/?s=abs&where=functions&lang=python'
text = re.sub('https://|http://', 'www.', text)
text = re.split('/', text, 1)[0]
print(text)"""
############################################
text = 'How the Avocado Became the Fruit of the Global Trade'

print(f"#{' #'.join(sorted(text.split(), key=len,reverse=True)[:3])}")
