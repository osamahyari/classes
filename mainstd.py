import csv
import mysql.connector
from student import Student
#import ipdb; ipdb.set_trace()
koko = 0   
list = []
with open('students.csv','r') as csvFile:
    reader = csv.DictReader(csvFile)
  
    for row in reader:
        list.append(Student(**row)) 
        print(list)


            



csvFile.close()
    


#a , b , c , d , e = input('enter your firstname, lastname, phone, address, and major , while seperating each entity with 1 space\n').split()
#p1 = Student(a,b,c,d,e)
#p1.register()
