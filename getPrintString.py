class InputOutputString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

def test():
    Obj = InputOutputString()
    Obj.getString()
    Obj.printString()

test()

