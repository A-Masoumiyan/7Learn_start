def reader_gen(filename):
    for row in open(filename, 'r'):
        yield row


for row in reader_gen('messages.txt'):
    print(row)
