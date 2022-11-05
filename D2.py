msg_file = open('messages.txt', 'a')
msg_file.write('Hello world from ali\n')
msg_file.close()


with open('messages.txt', 'r') as file:
    msg=file.read()
print(msg)
