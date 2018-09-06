#Q1,2,3,4

import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cur=con.cursor()
    query1='create table students(Name varchar(20),Marks int(3))'
    cur.execute(query1)
    con.commit()
    l=[]
    for i in range(1,11):
        name=input('Enter name: ')
        marks=int(input('Enter marks: '))
        if marks in range(0,101):
            l.append((name,marks))
        else:
            marks=int(input('Enter marks b/w 0 and 100: '))
            l.append((name,marks))
    query2='insert into students(Name,Marks) values(?,?)'
    cur.executemany(query2,l)
    con.commit()
    query3='select * from students where Marks>80'
    cur.execute(query3)
    data=cur.fetchall()
    for row in data:
        print('Name: {}, Marks: {}'.format(row[0],row[1]))

except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Error: ',e)

finally:
    if cur:
        cur.close()
    if con:
        con.close()
    print('Table created successfully')
