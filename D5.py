# user_input = input('Enter your age :  ')
#
# try:
#     user_age = int(user_input)
#     user_data = open('user_data.csv', 'w')
# except (ValueError, NameError):
#     print('Invalid age')
# else:
#     print('Well done')
# finally:
#     print('process finish')
#     # user_data.close()
from utils2 import nest2


def nest():
    print('hello from nest 1')
    nest2()
    print('bye from nest 1')


try:
    nest()
except ValueError:
    print('value error raised')
