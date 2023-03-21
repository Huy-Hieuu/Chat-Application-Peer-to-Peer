import globals1
from test3 import change3

class change:
    def __init__(self) -> None:
        globals1.a += 1
        print(globals1.a)
        self.b = 1
    def loop(self):
        while True:
            self.b += 1

globals1.initGlobal()
a = change()
change3()
a.loop()