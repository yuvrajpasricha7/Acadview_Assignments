#Q1

area=lambda r: 4*3.14*r*r
r=int(input('Enter the radius of sphere: ')) #radius
print('Area={}\n'.format(area(r)))

#Q2

def perfect(num):
    sum=0
    for j in range(1,int(num/2)+1):
        if num%j==0:
            sum=sum+j
    if sum==num:
        return True

for i in range(1,1001):
    if perfect(i):
        print(i,'is a perfect number')

#Q3
def table(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)

n=int(input('\nEnter number: ')) #enter number to find its multiplication table
table(n)

#Q4

def power(m,n):
    if(n==1):
        return m
    else:
        return power(m,n-1)*m

a=int(input('\nEnter base : '))
b=int(input('Enter power: '))
print(a,'^',b,'=',power(a,b))