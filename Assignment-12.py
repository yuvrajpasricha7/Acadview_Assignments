#Q1

from datetime import date
print(date.today().strftime('%A'))

#Q2

import webbrowser
song=input('\nEnter the name of the song: ')
webbrowser.open_new_tab('https://www.youtube.com/results?search_query=%s' % song)

#Q3

import os
i=1
os.chdir('/Users/mac/Desktop/dbms SS')
files=os.listdir('/Users/mac/Desktop/dbms SS')
for f in files:
    os.rename(f,'SS'+str(i)+'.jpg')
    i=i+1