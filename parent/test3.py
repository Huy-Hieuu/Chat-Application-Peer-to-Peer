import globals1

class change3:
    def __init__(self) -> None:
        globals1.a += 1
        print(globals1.a)
        self.b = 1
    def loop(self):
        while True:
            self.b += 1