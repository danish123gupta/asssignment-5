#q.no.1
print("the time tuple returned by localtime and gmtime contains year,month,day,hour,minuteand so on")

#q.no.2

import time
localtime = time.asctime(time.localtime(time.time()))
print("local current time:",localtime)



#q.no.3


import datetime
i = datetime.datetime.now()
print("current month = %s" %i.month)


#q.no.4
import datetime
i = datetime.datetime.now()
print("current day = %s" %i.day)




#q.no.5
import datetime
mydate= datetime.date(2021,1,11)
print(mydate.strftime("%A"))


#Q.NO.6
import time
localtime = time.localtime(time.time( ))
print("local current time:",localtime)


#q.no.7
import math
n=int(input("enter number:"))
print (math.factorial(n))

#q.no.8
import math
n=int(input("enter number:"))
m=int(input("enter number:"))
print (math.gcd(n ,m))


#q.no.9
import os
print(os.getcwd())
print(os.environ)










