# TAMRIN JALASAT FOLDER 04 7LEARN
###########################################
# TAMRIN (1) ==> ODD AND EVEN

"""odd = list()
even = list()
for i in range(1, 51):
    if i % 2 == 0:
        even.append(i)
    if i % 2 == 1:
        odd.append(i)

even2 = [i for i in range(1, 51) if i % 2 == 0]
odd2 = [i for i in range(1, 51) if i % 2 != 0]
print(odd, even, '\n', odd2, even2, sep='\n')"""

#################### END #######################
# TAMRIN (2) ==> BARNA ME I KE ADAD + RA AZ - TASHKHIS DAHAD

"""num = int(input('Enter a number : '))
print("MOSBAT" if num > 0 else "MANFI")
"""

# TAMRIN (3) ==> BARNAME I KE AZ KARBAR VORUDI BEGIRAD VA BE TEDAD DELKHAH BARAYASH CHAP KONAD

"""txt = input("Please Enter Your Text :  ")
number = int(input("Enter A Number :  "))
print((txt + '\n') * number)

for i in range(number):
    print(txt)"""

# TAMRIN (4) ==> TAEEN BOZORG TARIN ADAD

"""
num_list = list(input('Please Enter Range Number :  ').replace(" ", ""))
print(sorted(list(map(int, num_list)))[-1])
"""

# TAMRIN (5) ==> TARIKH RA BA FORMATI KHAS PRINT KONAD

"""from datetime import datetime
from time import sleep
from os import system

while True:
    time = datetime.now()
    print(f'{time.year}/{time.month}/{time.day}\t{time.hour}:{time.minute}:{time.second}')
    sleep(1)
    system("clear")
    """
# TAMRIN (6) ==> BARNAME I KE MANAND SYSTEM YEK KETAB KHANE AMAL KONAD
'''from books import books


def add_book(nevisande, motarjem, *Books):
    books.append({nevisande: {'motarje': motarjem, 'Books': list(Books)}})



add_book(input('please enter name nevisande: '),
         input('please enter name motarjem: '),
         input('please enter books list: ')
         )

for book in books:
    print(books[book])

fin = input("enter book name or nevisande or motarjem : ")

if fin in books.keys():
    # print(fin + ":", books.get(fin))
    print(f"""
nevisande : {fin} 
motarjem :  {books.get(fin)['motarjem']}
books :  {" ".join(books.get(fin)['Books'])}
""")
for d in books.keys():
    if fin in books[d]['Books']:
        # print(d, books[d])
        print(f"""
        nevisande : {d} 
        motarjem :  {books[d]['motarjem']}
        books :  {" ".join(books[d]['Books'])}
        """)
    if fin in books[d]['motarjem']:
        print(f"""
                nevisande : {d} 
                motarjem :  {books[d]['motarjem']}
                books :  {" | ".join(books[d]['Books'])}
                """)
'''
# TAMRIN (7) ==> MASHIN HESAB
# eval()

