def filter_numbers():
    # return [i for i in range(100) if i % 7 == 0]
    tmp = list()
    for i in range(100):
        if i % 7 == 0:
            tmp.append(i)

    print('hello from filter numbers')
    return tmp

#
# numbers = filter_numbers()
# for num in numbers:
#     print(num)


def filter_numbers_generator():
    for i in range(100):
        if i % 7 == 0:
            yield i
    print('hello from filter numbers generator')


numbers_generator = filter_numbers_generator()
for num in numbers_generator:
    print(num)
