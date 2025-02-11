class father:
    def football(self):
        print("father likes to watch football")
class mother:
    def cooking(self):
        print("mother likes cooking")


class Boy(father):
    def Boyage(self):
        print("A boy is 15 years old")
my_boy=Boy()
my_boy.football()
my_boy.Boyage()

class girl(mother):
    def eating(self):
        print("The girl likes eating")
girl_child=girl()
girl_child.cooking()
girl_child.eating()

