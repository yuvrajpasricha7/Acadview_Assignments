#Q1

class circle:
    r=int(input('Enter radius: ')) #radius

    def getArea(self):
        self.area=4*3.14*self.r*self.r
        print('Area={}'.format(self.area))

    def getCircumference(self):
        self.circum=2*3.14*self.r
        print('Circumference={}'.format(self.circum))

c1=circle()
c1.getCircumference()
c1.getArea()

#Q2

class student:
    def __init__(self):
        self.name=input('\nEnter name: ')
        self.rollno=input('Enter roll no.: ')

    def setAge(self):
        self.age=input('Enter age: ')

    def setMarks(self):
        self.marks=input('Enter marks: ')

    def display(self):
        print('Name={}\nRoll no.={}\nAge={}\nMarks={}'.format(self.name,self.rollno,self.age,self.marks))

s1=student()
s1.setAge()
s1.setMarks()
s1.display()

#Q3

class temperature:
    def convertFahrenheit(self,c):
        print('Fahrenheit=',c*1.8+32)

    def convertCelsius(self,f):
        print('Celsius=',(f-32)/1.8)

t=temperature()
c=int(input('\nEnter temperature in celsius: '))
t.convertFahrenheit(c)
f=int(input('Enter temperature in fahrenheit: '))
t.convertCelsius(f)

#Q4

class MovieDetails:

    def add(self):
        self.artistName=input('\nEnter artist name: ')
        self.year=input('Enter year of release: ')
        self.rating=input('Enter ratings: ')

    def display(self):
        print('Artist name: {}\nYear of release: {}\nRatings: {}'.format(self.artistName,self.year,self.rating))

m=MovieDetails()
m.add()
m.display()

#Q5

class Animal:

    def animal_attribute(self):
        print('\nIn animal class')

class Tiger(Animal):

    def tiger(self):
        print('In tiger class')

t1=Tiger()
t1.animal_attribute()

#Q6

'''Output= A B
           A B'''

#Q7

class Shape:

    def __init__(self):
        self.length=int(input('\nEnter length: '))
        self.breadth=int(input('Enter breadth: '))

    def area(self):
        if self.length==self.breadth:
            print('Area of square=',self.length*self.breadth)
        else:
            print('Area of rectangle=',self.length*self.breadth)

class Square(Shape):

    def __init__(self):
        super().__init__()


class Rectangle(Shape):

    def __init__(self):
        super().__init__()

s2=Square()
s2.area()
r=Rectangle()
r.area()