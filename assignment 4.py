#TUPLE
#Q.NO.1
t=(1,2,"a" ,[12,34])
print(len(t))

#Q.NO.2
t1 = (23,45,12,78,61)
print(max(t1))
print(min(t1))

#Q.NO.3
t2 = (2,4,6,8)
j= 1
for i in t2:
    j= i*j
print(j)

#sets
#q.no.1
a= input("enter value")
b= input("enter value")
c= input("enter value")
d= input("enter value")
e= input("enter value")
s1= set([a,b,c])
s2 = set([d,e])

#q.no.2
s3 = s1 -s2
print(s3)

#q.no.3
#comparision between two sets
print(s1>=s2)
print(s2<=s1)

#intersection of sets
print(s1&s2)

#dictionary
#q.no.1
name = input("enter name")
marks1 = input("enter marks")
d1 = {"name":name ,"marks":marks1}
print(d1)

#q.no.2
marks = {"a": 45 ,"b":67 ,"c":90 ,"d":23 ,"e":99}
z= sorted(marks.items(),key=lambda t:t[1])
print(dict(z))

#q.no.3
l= ["M","I","S","S","I","S","S" ,"I","P","P","I"]
m= l.count("M")
i= l.count("I")
s= l.count("S")
p= l.count("P")
d2 ={"M":m,"I":i,"S":s, "P":p}
print(d2)





