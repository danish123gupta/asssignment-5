#q.no.1
""""l=[]
   for a in range (10):
    integer=int(input("enter number:"))
    l.append(integer)
print(l)
for b in l:
    print(b)





    #q.no.2
while True:
 print("infinite")



  #q.no.3))

m=[]
elements = int(input("enter total number of elements of list:"))
for c in range (elements):
    element = int(input("enter elements:"))
    m.append(element)
print(m)
n =[]
for d in m:
    e= d **2
    n.append(e)
print(n)



#Q.NO.4

integers=[]
decimals=[]
strings=[]
lists =["danish","3","4","6","gupta","6"]
for f in lists:
    if f.isalpha():
        strings.append(f)
    elif f.isdigit():
        integers.append(int(f))
    else:
        decimals.append(float(f))
print(decimals)
print(integers)
print(strings)



#q.no.5

ev_li=[]
od_li =[]
for i in range(1,101):
    if(i%2==0):
        ev_li.append(i)
else:
    od_li.append(i)
print("even list:" , ev_li)
print("odd list:"  ,od_li)


#q.no.6
i=1
while i<=4:
    print ("*"*i)
    i=i+1



#q.no.7
dict1 = {}
elements = int(input("enter no of elements:"))
for i in range(elements):
    key = input("enter key:")
    value= input("enter value:")
    dict1[key]=value
print(dict1)
for key in dict1:
    print(key)
    """


#q.no.8
l= []
a= int(input("enter total number of elements:"))
for b in range(a):
    elements = input("enter element:")
    l.append(elements)
c=input("enter elements to be search:")
for d in l:
    if c==d:
        l.remove(c)
        print(l)