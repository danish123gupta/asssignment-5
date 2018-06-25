#q.no.1
class Animal():
     def animalname(self):
         print("wolf")

class Tiger(Animal):
     def color(self):
         print("brown")

brown= Tiger()
brown.animalname()

#q.no.2
#the output of the code is 'A' and 'B'
#the output of the code is 'A' and 'B'

#q.no.3

class Cop():
    name = input("enter name: ")
    age = int(input("enter age: "))
    work_experience = int(input("enter work experience: "))
    designation = input("enter designation: ")
    def __init__(self, ):
        pass

    def add(self):
        place=input("enter place: ")
        self.place=place

    def dispaly(self):
        print("name is: ",self.name)
        print("age is: ",self.age)
        print("work experience is of ",self.work_experience)
        print("designation is:",self.designation)
        print("working place: ",self.place)

    def update(self):
        print("to update the information:-")
        name=input("enter name: ")
        self.name=name
        age=input("enter age: ")
        self.age=age
        work_experience=input("enter work experience: ")
        self.work_emperience=work_experience
        designation=input("enter designation: ")
        self.designation=designation
        place=input("enter working place: ")
        self.place=place
        print("updated information is:-")
        c.dispaly()

class Mission(Cop):
    def add_mission_detail(self):
        pass

c=Cop()
m=Mission()
c.add()
c.dispaly()
c.update()
m.update()



#Q.NO.4
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self):
        self.length =789456
    def area(self):
        return self.length*self.length
asq=Square()
print(asq.area())

class rectangle(Shape):
    def __init__(self):
        self.length =7
        self.width  =6
    def area(self):
        return self.length*self.width
arect=rectangle()
print(arect.area())



#







