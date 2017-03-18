class Human:
    def sayHello(self,id1, uname=None,password1=None):

        if uname is not None:
            print 'Hello... ' + uname
        elif id1==90:
            print id1
        else:
            print "ss"


# Create instance
obj = Human()

# Call the method
obj.sayHello(2)
obj.sayHello(22,'pop')
