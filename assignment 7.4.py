#q.no.1

class Circle():
    radius=int(input("enter radius:"))
    def __init__(self):
        pass
    def getarea(self):
        area=3.14*self.radius*self.radius
        print("area of circle is:",area)
    def getcircum(self):
        circum=2*3.14*self.radius
        print("circumference is:",circum)
c=Circle()
c.getarea()
c.getcircum()



#q.no.2

class Student():
    n=input("enter name:")
    r=int(input("enter rollno:"))
    def __init__(self):
        pass
    def getdisplay(self):
        print(self.n)
        print(self.r)
c=Student()
c.getdisplay()


#q.no.3


class Temperature():
    cel=float(input("enter temperature in celsius:"))
    feh=float(input("enter temperature in farenheit:"))
    def __init__(self):
     pass
    def convert_cel(self):
        f=self.cel*(9/5)+32
        print("temperature in farenheit",f)
    def convert_feh(self):
        c=(self.feh-32)*(5/9)
        print("temperature in celsius",c)
t=Temperature()
t.convert_cel()
t.convert_feh()


#q.no.5
""""""
class Expenditure():
    expense=float(input("enter expenditure:"))
    save=float(input("enter savings:"))
    def __init__(self):
     pass
    def display(self):
        print("expenditure is:",self.expense)
        print("saving is:",self.save)
    def cal_salary(self):
        total_salary=self.expense+self.save
        return total_salary
    def dis_salary(self):
        print("total salary is:",e.cal_salary())
e=Expenditure()
e.display()
e.cal_salary()
e.dis_salary()




class Movie():
    def __init__(self):
        pass
    def display(self,movieName,artistName,yearofRelease):
        self.m= movieName
        self.a= artistName
        self.y =yearofRelease
        print(self.m,self.a,self.y)
    def update(self,movieName,artistName,yearofRelease):
        self.m=  input("enter the movie name:")
        self.a = input("enter the artist name:")
        self.y = input("enter the year of release:")
        print(self.m,self.a,self.y)
y=Movie()
y.display("jackpot:","akshay kumar","20 may 2012")
t=Movie()
t.update("m","a","y")




