file=open("fftt.txt","r")
print (file.read())

file=open("fftt.txt","r")
print(file.read(5))

file = open("fftt.txt","r")
print( file.readline())

file = open("fftt.txt","r")
print( file.readline(3))

file = open("fftt.txt","r")
print( file.readlines())

file.close()


with open ("fftt.txt")as file:
    data=file.read()
do something

