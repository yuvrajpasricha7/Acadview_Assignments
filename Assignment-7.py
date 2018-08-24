#Q1

d1={}
n1=int(input('Enter the no. of keys in dict: '))
for i in range(1,n1+1):
    d1[i]=input('Enter value: ')
m=input('Enter the value whose key you want to search: ')
for k1 in d1.keys():
    if d1[k1]==m:
        print(k1)
        break
else:
    print('Key not found')

#Q2

d2={} #empty list
n2=int(input('Enter the no. of students: '))
for i in range(1,n2+1):
    d3={}
    n=input('Enter name: ') #name of student
    n3=int(input('Enter the no. of subjects: '))
    for j in range(1,n3+1):
        s=input('Enter sub: ') #subject
        m=int(input('Enter marks: ')) #marks
        d3[s]=m
    d2[n]=d3
name=input('Enter the name of the student whose marks you want to find: ')
for k in d2.keys():
    if name==k:
        print(d2[name])
        break
else:
    print(name,'not in dictionary')