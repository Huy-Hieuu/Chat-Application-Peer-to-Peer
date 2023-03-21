import threading
import time

class classA:
    def __init__(self) -> None:
        self.a = 0
    def loop(self):
        threading.Thread(target=childOfA().print123).start()
        # print("before: " + str(self.a) + " " + str(id(self.a)))
        while True:
            self.a += 1
            time.sleep(0.5)
            print("parent A: " + str(self.a))

        print("after: " + str(self.a) + " " + str(id(self.a)))
    def getA(self):
        return self.a

class childOfA(classA):
    def __init__(self) -> None:
        super().__init__()

    def print123(self):
        while True:
            
            print("child Of A: " + str(self.getA()))
            time.sleep(0.5)

if __name__ == '__main__':
    A = classA()
    B = classA()

    threading.Thread(target=A.loop).start()
    # time.sleep(2)
    # print(A.getA())
    # threading.Thread(target=A.getA).start()