#Q1

import re
str1=input('Enter your email-id: ')
match1=re.finditer('^\w[_a-zA-Z0-9.yu]*@{1}(gmail.com|yahoo.com)$',str1)
m=0
for i in match1:
    m=i.group()
if str1==m:
    print('Email-id is valid')
else:
    print('Email-id is not valid')

#Q2

import re
str2=input('\nEnter your mobile no.: ')
match2=re.finditer('^[+]{1}[9]{1}[1]{1}[6-9]\d{9}',str2)
m=0
for i in match2:
    m=i.group()
if str2==m:
    print('It is a valid number')
else:
    print('It is not a valid number')