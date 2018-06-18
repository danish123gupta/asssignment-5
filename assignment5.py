#Q.NO.1
"""
year=int(input("enter year:"))
if year % 4 == 0 and year % 100!=0:
    print(year,"is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 400 ==0:
    print(year, "is  a leap year")
else:
    print(year,"is not a leap year")

#question.no.2

l=int(input("enter  the length"))
b=int(input("enter the breadth"))
if(l==b):
    print("square")
else:
    print("rectangle")





#QUESTION 3
print("enter the first age")
first = input()
print ("enter the second age")
second = input()
print ("third age")
third = input()
if first >= second and first >= third:
    print ("oldest is",first)
elif second >= first and second >= third:
    print ("oldest is",second)
elif third >= first and third >= second:
    print ("oldest is",third)
else:
    print ("all are equal")


    #q.no.4
a=int(input("enter the point scored"))
if(a>=1)and(a<=50):
    print("sorry this time no prize")
elif(a>=51)and(a<=150):
    print("your prize is a wooden dog")
elif(a>=151)and(a<=180):
    print("your prize is book")
elif (a>=181)and (a<=200):
    print("your prize is chocolate")
else:
    print("invalid score")

"""
#q.no.5
quantity=int(input("enter quantity: "))
if (quantity*100>1000):
    print ("cost is",((quantity*100)-(0.1*quantity*100)))
else:
    print ("cost is",quantity*100)















