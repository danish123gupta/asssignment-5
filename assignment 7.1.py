#q.no.1
"""
radius=float(input("enter number:"))
def area (rad):
    area=3.14*rad*rad
    return area
ar= area(radius)
print(ar)



#q.no.2
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
for i in range(1,1001):
    if(perfect(i))==True:
        print(i)





        #q.no.3
num = int(input("display multiplication table of?"))
for i in range(1,11) :
    print(num,'x',i,'=',num*i)



    #q.no.4
def power(a,b):
     if b == 1:
         return a
     else:
         return a* power(a,b-1)
print(power(2,3))
    """


#q.no.5
d= {}
def fact(a):
    f=1
    for i in range(1,a+1) :
        f=f*i
        return f
n=int(input("enter a number:"))
d[n]= fact(n)
print(d) 





