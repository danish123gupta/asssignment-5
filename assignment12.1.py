#Q.NO.1
try:
    a=3
    if(a<4):
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("number is divided by zero")

#Q.NO.2

try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("index out of range")

#Q.NO.3
try:
    raise NameError("HI THERE")
except NameError:
    print("an exception")

#Q.NO.4
# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


#q.no.5
#import error
try:
    import danish
    a=[1,2,3]
    print(a[3])
except ZeroDivisionError:
    print("number is divided by zero")
except ModuleNotFoundError:
    print("file doesnot exist")

#value errror
try:
    print ("hello world")
except ValueError:
    print("a shorr description for value error")

#index error
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("index out of range")

#q.no.6

class AgeTooSmall(Exception):
    pass
value = True
while value:
    try:
        a=int(input("enter age:"))
        if a<18:
            raise AgeTooSmall
    except ValueError:
        print("please enter integer:")
    except AgeTooSmall:
        print("Age less than 18")
    else:
        print("you are egligible")
        value= False









