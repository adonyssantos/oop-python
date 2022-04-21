class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, world!")

    def get_name(self):
        return self.name


p1 = Person("John", 30)
p1.greet()
print(p1.get_name())
