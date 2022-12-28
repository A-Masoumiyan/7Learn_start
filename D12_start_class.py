class Customer:
    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email

    def login(self):
        pass


class Product:
    def __init__(self, upc, name, price=0, description=''):
        self.upc = upc
        self.name = name
        self.price = price
        self.description = description


c1 = Customer('hossein', '1224', 'hossein', 'hossein@gmail.com')
c2 = Customer('ali', '1224', 'masoumian', 'ali@gmail.com')
print(c1.username)
print(c2.username)

p1 = Product(1, 'product#1')
p2 = Product(1, 'product#2', 1000)
p3 = Product(1, 'product#2', 1000, 'some description about product')
print(p1)
