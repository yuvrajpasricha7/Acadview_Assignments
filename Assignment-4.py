#Q1

l1=[1,2,3,4,5]
l1.reverse()
print(l1)

#Q2

str2=input('\nenter string: ') #string
for i in str2:
    if(i.isupper()):
        print(i,end=' ')

#Q3

l3_new=[]
str3=input('\n\nenter input: ').split(',')
for i in str3:
    l3_new.append(int(i))
print(l3_new)

#Q4

str4=input('\nEnter string: ') #string
str=str4[: :-1] #reversed string
if(str==str4):
    print('Palindromic string\n')
else:
    print('Not a palindromic string\n')

#Q5

import copy as c
l5=[1,2,[3,4],5]
l=c.deepcopy(l5)
l[2][0]=6
'''In deep copy changes in l will not affect l5 whereas in shallow copy, 
if original object contains any reference to mutable object,then the 
duplicate reference variables willbe created pointing to old contained object 
but no duplicate objects will not be created'''
print(l5,l,sep='\n')




