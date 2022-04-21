class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


p1 = Product("Shirt", 10)
print(p1.price)

# this throws an error
# p1.price = -1
# print(p1.price)

p1.price = 20
print(p1.price)
