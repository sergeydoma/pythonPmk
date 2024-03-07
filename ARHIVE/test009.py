from threading import Thread


# from exchange import exchang as ex


class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print ('A')

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print ('B')
            # ex()
myClassA()
myClassB()
while True:
    pass