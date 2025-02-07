# object oriented programmming
class Person:
    def __init__(self,name,age):
        # this is the constructor method
        # It takes two parameters and intializes them as attribute
        self.name = name
        self.age = age


    def myfunction(self):
          print( f"Hello my name is {self.name} and my age is {self.age}")
          # this is a method fumction
# create am object or instance of class
myobject= Person("Vito",30)
myobject.myfunction()
myobject= Person("Sonny",25)
myobject.myfunction()
myobject= Person("Johnny",21)
myobject.myfunction()
myobject= Person("Corleone",50)
myobject.myfunction()
myobject= Person("Brazine",43)