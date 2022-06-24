class Base:
    def __init__(self, name):
        self.name = name

    def presentarse(self):
        return f"Hola, soy {self.name}, de la clase {self.__class__}"

class SegundaBase:
    def __init__(self, salary):
        self.salary = salary

    def presentarse(self):
        return f"Adios amistad, se despide {self.name}"

class Person(SegundaBase, Base):
    def __init__(self, name, age, salary):
        # super().__init__(name, salary)
        Base.__init__(self, name)
        SegundaBase.__init__(self, salary)
        self.age = age
