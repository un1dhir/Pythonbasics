# Using OOPs create a class called cars which have the following atributes
# colour,model and year manufacture
# implement constructor method and a method fumction fumctions that prints("MY FAVOURITE CAR IS -MODEL,IT IS THIS IN -COLOUR AND MANUFACTURED IN -YEARS")
# CREATE 5 INSTANCE OF THAT CLASS




class Cars:
    def __init__(self,model,colour,year):
        self.model= model
        self.colour= colour
        self.year= year

    def carfunction(self):
        print(f"I own a {self.model} which is {self.colour} and was manufactured in the year {self.year}")

mymodel= Cars("Mercedes","Grey",2019)
mymodel.carfunction()
mymodel= Cars("Porche","Black",2007)
mymodel.carfunction()
mymodel= Cars("Ferari","Red",2011)
mymodel.carfunction()
mymodel= Cars("Aston MArtin","Brown",2014)
mymodel.carfunction()



