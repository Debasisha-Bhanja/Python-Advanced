
class Car:
    def __init__(self):
        pass

    def _drive(self):
        print 'driving'

    def __updateSelfs(self):
        print 'updating myself'


redcar = Car()
redcar.drive()
#redcar._updateSelfs()