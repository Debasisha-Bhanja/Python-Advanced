class User:
    name = ""
    def __init__(self, name):
        self.name = name

    def printName(self):
        print "Name  = " + self.name

class Programmer(User):
    def __init__(self, name):
        self.name = name

    def printName(self):
        print "NameProgrammer  = " + self.name


brian = User("Srinivas")
brian.printName()

diana = Programmer("Kolaparthis")
diana.printName()
