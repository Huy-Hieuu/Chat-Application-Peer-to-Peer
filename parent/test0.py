import globals1
import threading
import time

lock = threading.Lock()

class change:
    def __init__(self) -> None:
        # globals1.initGlobal()
        pass
    def loop(self):
        lock.acquire()
        globals1.initGlobal()
        print("before: " + str(globals1.a) + " " + str(id(globals1.a)))
        for i in range(1000000):
            globals1.a += i
        print("after: " + str(globals1.a) + " " + str(id(globals1.a)))
        lock.release()

if __name__ == '__main__':
    # globals1.initGlobal()

    threading.Thread(target=change().loop).start()
    threading.Thread(target=change().loop).start()
    A = change()
    B = change()
    threading.Thread(target=A.loop).start()
    threading.Thread(target=B.loop).start()
