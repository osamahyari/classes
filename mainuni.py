import csv
import mysql.connector
from uni import University
#import ipdb; ipdb.set_trace()
koko = 0   
list = [ ]
mydb = mysql.connector.connect(
    host = 'localhost' ,
    user = 'root' ,
    passwd = 'hiyarI10' ,
    database = 'task'
)    
mycursor = mydb.cursor()
sql = 'INSERT INTO university (courses, majors, students, teachers) VALUES (%s, %s, %s, %s)'
val = []
with open('uni.csv','r') as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
        print(row)
        if koko > 0 :
            val = row 
            mycursor.execute(sql, val)
        koko +=1

mydb.commit()
csvFile.close()