class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' make noise')

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print(self.name + ' barks')

    def parent_speak(self):
        super().speak()

    def get_age(self):
        print(self.age)

animal = Animal('generic Animal')
animal.speak()

dog = Dog('Dog', 32)
dog.speak()
dog.parent_speak()
dog.get_age()