# zip in python 7learn
from data.data import words


# a = 'abc'
# b = 'def'
# c = 'ghi'
#
# f = list(zip(a, b, c))
# print(f)
# s = list(zip(*f))
# print(s)
def find_common_prefix(words_list):
    s = tuple(zip(*words))
    tmp = ''
    for i in s:
        if len(set(i)) != 1:
            break
        tmp += i[0]
    return tmp


print(find_common_prefix(words))
