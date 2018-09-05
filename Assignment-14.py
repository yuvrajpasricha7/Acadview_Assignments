#Q1

l=[1,2,3,4,5]
l1=[i**3 for i in l]
print(l1)

#Q2

n1=int(input('\nEnter lower bound: '))
n2=int(input('Enter upper bound: '))
l2=[i for i in range(n1,n2+1) if all(i%y!=0 for y in range(2,int(i/2)+1)) and i!=1]
print(l2)

#Q3

'''Generator Expressions are somewhat similar to list comprehensions, but the former doesn’t
construct list object. Instead of creating a list and keeping the whole sequence in the memory,
the generator generates the next element in demand'''

#Q4

Celsius=[39.2,36.5,37.3,37.8]
l4=list(map(lambda x: x*9/5+32,Celsius))
print(l4)

#Q5

l=[1,2,3,4,5]
l5=list(map(lambda x:x*x,l))
print(l5)

#Q6

l=[1,2,3,4,5,6,7,8,9,10]
l6=list(filter(lambda x: x if all(x%y for y in range(2,int(x/2)+1)) and x!=1 else False,l))
print(l6)

#Q7

from functools import *
l=[1,2,3,4,5]
l7=reduce(lambda x,y: x*y,l)
print(l7)