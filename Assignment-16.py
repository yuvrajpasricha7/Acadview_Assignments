import pymongo
client=pymongo.MongoClient()
db=client['student']
col=db['student_table']
for i in range(0,11):
    name=input('Enter name: ')
    marks=int(input('Enter marks: '))
    stu={'name: ':(name),'marks: ':(marks)}
    col.insert_one(stu)
data=col.find({'marks: ':{'$gt':80}})
for row in data:
    print(row)