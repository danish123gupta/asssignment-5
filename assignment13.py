f=open("test.txt","r")
print(f)
print(f.read(5))
print(f.readline())


#f=open("test.txt","a")
#print(f)
#print(f.read)
#print(f.readline())
#f.write("hello")

#l=["a\n","b\n","c\n"]
#f.writelines(l)


#with open("test.txt","r") as f:
# f.read()
#  f.readlines()


#f=open("test.txt","r")
#print(f)
f= open("test.txt","r")
print(f.read(5))
f.seek(0)
print(f.tell())


