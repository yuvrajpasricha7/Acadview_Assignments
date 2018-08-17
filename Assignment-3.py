#List

#Q1
l1=[] #empty list
n=int(input('Enter the no. of elements in the list'))
for i in range(0,n):
    j=input() #enter the element
    l1.append(j)
print(l1)

#Q2
l2=['google','apple','facebook','microsoft','tesla']
l1.extend(l2)
print(l1)

#Q3
l3=[] #empty list
m=int(input('Enter the no. of elements in the list'))
for i in range(0,m):
    j=input() #enter the element
    l3.append(j)
obj=input('enter the object') #enter the object which you want to count
print('count=',l3.count(obj))

#Q4
l4=[] #empty list
n1=int(input('Enter the no. of elements in the list'))
for i in range(0,n1):
    j=int(input()) #enter the element
    l4.append(j)
l4.sort()
print(l4)

#Q5
a=[] #empty list1
b=[] #empty list2
c=[] #empty list3
n2=int(input('Enter the no. of elements in the list'))
for i in range(0,n2):
    j=int(input()) #enter the element for list1
    a.append(j)
print('Enter elements for list 2')
for i in range(0,n2):
    k=int(input()) #enter the element for list2
    b.append(k)
c=a+b
c.sort()
print(c)

#Q6
even=0 #counter for even nos.
odd=0 #counter for odd nos.
for i in c:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print('even nos.=',even)
print('odd nos.=',odd)

#Tuples

#Q1
t1=(2,4,6,8,10)
print(t[::-1])

#Q2
t2=(1,3,5,7,9)
print('max=',max(t2))
print('min=',min(t2))

#Strings

#Q1
str1=input('Enter string')
print(str1.upper())

#Q2
str2=input('Enter string')
if(str2.isdigit()):
    print('true')
else:
    print('false')

#Q3
str3='Hello World'
str3=str3.replace('World','Yuvraj')
print(str3)
