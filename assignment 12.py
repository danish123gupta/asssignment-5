try:
    import danish
    a=[1,2,3]
    print(a[3])
except ZeroDivisionError:
    print("number is divided by zero")
except ModuleNotFoundError:
    print("file doesnot exist")


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

try:
    raise NameError("HI THERE")
except NameError:
    print("an exception")

