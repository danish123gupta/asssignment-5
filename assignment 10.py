#q.no.1
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i
    def run(self):
        time.sleep(5)
        print("thread basics",self.h)
thread1 = mythread(1)
thread1.start()
thread2 = mythread(2)
thread2.start()



#q.no.2

import threading
from threading import Thread
import time
def loop():
    for i in range(1,11):
        time.sleep(1)
        print("i")
threading.Thread(target=loop).start()


#q.no.3


import threading
from threading import Thread
import time
class Threads(threading.Thread):
       def __init__(self,list1):
           threading.Thread.__init__(self)
           self.list1=list1


       def run(self):
          count=0
          for i in self.list1:
            count +=2
            time.sleep(count)
            print(i)

list1=[]
n=int(input("enter total no. of elements: "))
for i in range(n):
    j=input("enter element: ")
    list1.append(j)

t=Threads(list1)
t.start()

#Q.NO.4

import threading
import time
import math

class Fact(threading.Thread):
    def __init__(self,f):
        threading.Thread.__init__(self)
        self.f=f
    def run(self):
        print("factorial of ",self.f,"is",math.factorial(self.f))

f=int(input("enter a number: "))
f1=Fact(f)
f1.start()
