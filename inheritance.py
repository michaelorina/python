class person:

    def __init__ (self, name, age):
        self.name = name
        self.age = age

        print('The name is {} and the age is {}'.format(self.name, self.age))

class teacher(person):
    def print(self, name, age):
        person.__init__(self,name,age)

class student(person):
    def print(self,name,age):
        person.__init__(self,name,age)        