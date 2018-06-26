import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i
    def run(self):
        time.sleep(5)
        print("value send",self.h)
thread1 = mythread(1)
thread1.start()
thread2 = mythread(2)
thread2.start()

class mythread(threading.Thread):
    def _init__(self ,i):
        threading.Thread.__init__(self)
        self.h = i
    def run(self):
        print("no is" , self.h)

    for i in range(10):
        thread1 = mythread(1)
        thread1.start ()
        time.sleep(1)
print("active threads are ",threading.activeCount())

def sleepMe(i):
    print("thread%i going to sleep for five seconds" %i)
    time.sleep(5)
    print("thread %i is awake now" %i)
    for i in range(10):
        th= Thread(target=sleepMe ,args =(i, ))
