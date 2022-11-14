# TAMRIN JALASAT FOLDER 04 7LEARN
"""
num = 123456789
num = list(str(num))
num2 = ''
for i in range(len(num)):
    num2 += num.pop()
print(int(num2))
"""

######################
"""card_number = '6219 8619 0807 4643'
card_number = card_number.replace(' ', '')
tmp = ''
co = 0
for i in card_number:
    if 4 <= co < 12:
        if co == 8 or co == 4:
            tmp += '-'
            tmp += '*'
        elif co == 11:
            tmp += '*'
            tmp += '-'
        else:
            tmp += '*'
    else:
        tmp += i
    co += 1
print(tmp)
"""

"""card_number = '6219 8619 0807 4643'
card_number = card_number.replace(' ', '')
card_number = card_number.replace(card_number[4:12], "-****-****-")
print(card_number)
"""