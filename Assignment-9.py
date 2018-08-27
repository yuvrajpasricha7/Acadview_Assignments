#Q1

#Exception occured in the program is Zero Division Error
a=3
if a<4:
    try:
        a=a/(a-3)
    except ZeroDivisionError as msg:
        print(msg)

#Q2

#Exception occured in the program is Index Error
l=[1,2,3]
try:
    print(l[3])
except:
    print('\nList index out of range\n')

#Q3

#Output= An exception

#Q4

'''Output= -5.0
           a/b result in 0'''

#Q5

#1.Import Error
try:
    import randm
    l1=[1,2]
    random(l1)
except ImportError as mssg:
    print(mssg)

#2.Value Error
try:
    a=int(input('Enter integer: '))
except ValueError as mssg1:
    print(mssg1)
else:
    print('no error')

#3.Index Error
l3=[4,5]
try:
    print(l3[2])
except IndexError as mssg2:
    print(mssg2)