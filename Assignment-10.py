#file.txt
'''hello
   my name is
   yuvraj singh'''

#file2.txt
'''abc de 
   fgh ijk
   lmn'''

#Q1
n1=int(input('Enter the no. of lines you want to read: '))
f1=open('file.txt','r')
l1=f1.readlines()
for i in range(0,n1):
    print(l1[i])
f1.close()
print('\n')

#Q2

d2={}
f2=open('file.txt','r')
l2=f2.read().split()
for i in l2:
    if i in d2:
        d2[i]=d2[i]+1
    else:
        d2[i]=1
for k in d2.keys():
    print('frequency of',k,'=',d2[k])
f2.close()

#Q3

f3=open('file.txt','r')
data=f3.read()
f4=open('file1.txt','w')
f4.write(data)
f4.close()
f3.close()
print('\n')

#Q4

f5=open('file.txt','r')
f6=open('file2.txt','r')
l1=f5.read().split('\n')
k1=f6.read().split('\n')
for l,k in zip(l1,k1):
    print(l,k)
f6.close()
f5.close()
print('\n')

#Q5

l4=[]
f7=open('file3.txt','w')
for i in range(1,11):
    n=input('Enter number: ')
    f7.write(n + ' ')
f7.close()
f7=open('file3.txt','r')
l3=f7.read().split()
for i in l3:
    j=int(i)
    l4.append(j)
f7.close()
l4.sort()
f8=open('file4.txt','w')
for j in l4:
    f8.write(str(j)+' ')
    print(j)
f8.close()