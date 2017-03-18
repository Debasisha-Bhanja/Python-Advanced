class Human:
    def __init__(self):
        self.name = 'Humans'
        self.head = self.Head()

    class Head:
        def talk(self):
            return 'talking...'


if __name__ == '__main__':
    gui = Human()
    print gui.name
    print gui.head.talk()