#Q1

year=int(input('Enter year: ')) #enter the year you want to check
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,'is a leap year')
        else:
            print(year,'is not a leap year')
    else:
        print(year,'is a leap year')
else:
    print(year,'is a not leap year')

#Q2

l=int(input('\nEnter length: ')) #length
b=int(input('Enter breadth: ')) #breadth
a=l*b #area
if a==l*l:
    print('Dimensions are of square')
else:
    print('Dimensions are of rectangle')

#Q3

a1=int(input('\nEnter age of A: ')) #age of 1st person
a2=int(input('Enter age of B: ')) #age of 2nd person
a3=int(input('Enter age of C: ')) #age of 3rd person
if a1>a2:
    if a2>a3:
        print('A is the oldest','C is the youngest',sep='\n')
    elif a1>a3:
        print('A is the oldest','B is the youngest',sep='\n')
    else:
        print('C is the oldest','B is the youngest',sep='\n')
elif a1>a3:
    print('B is the oldest', 'C is the youngest', sep='\n')
elif a2>a3:
    print('B is the oldest','A is the youngest',sep='\n')
else:
    print('C is the oldest','A is the youngest',sep='\n')

#Q4

age=int(input('\nEnter age: ')) #age
sex=input('Enter sex(M or F): ') #gender
m_status=input('Enter marital status(Y or N): ') #marital status
if sex=='F':
    print('She can only work in urban areas.')
else:
    if age in range(20,41):
        print('He may work anywhere.')
    elif age in range(41,61):
        print('He can only work in urban areas.')
    else:
        print('ERROR')

#Q5

n=int(input('\nEnter quantity: ')) #quantity
total=100*n
if(total>1000):
    total=total-(0.1*total)
    print('total cost is',total,'\n')
else:
    print('total cost is',total,'\n')

#Q6

for i in range(0,10):
    j=input('Enter number: ')
    print(j)

#Q7
#infinite loop
a=1
while(a==1):
    print(a)

#Q8

l2=[]
l1= list(map(int,input('\nEnter the elements: ').split()))
for i in l1:
    l2.append(i*i)
print(l2)

#Q9
l4,l5,l6=[],[],[] #empty lists
l3=input('\nenter elements: ').split()
for i in l3:
    if i.isdigit():
        l4.append(int(i))
    elif i.isalpha():
        l5.append(i)
    else:
        l6.append(float(i))
print('int:',l4,'string:',l5,'float:',l6,sep='\n')

#Q10

l7=[] #empty list
flag=1
for i in range(1,101):
    if i>1:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
            else:
                flag=0
    if flag==0:
        l7.append(i)
print('\nprime nos. are=',l7)

#Q11

for i in range(1,5):
    for j in range(1,i+1):
        if j==i:
            print('*')
        else:
            print('*',end=' ')

#Q12

l8=list(input('\nEnter elements in list: ').split()) #list
num=input('Enter element: ') #element to be searched
for i in l8:
    if i==num:
        l8.remove(i)
        print(l8)
        break
else:
    print('Element not found')
