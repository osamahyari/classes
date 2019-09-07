import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost' ,
    user = 'root' ,
    passwd = 'hiyarI10' ,
    database = 'task'
)
sm = 0
koko = 0  
mycursor = mydb.cursor()
mycursor.execute("SELECT grade FROM exam WHERE course = 'math'")
myresult = mycursor.fetchall()

for x in myresult:
    x = int(x[0])
    sm = x + sm
    koko += 1
    
avg = sm / koko
sm = 0
koko = 0
print('math average is ')
print(avg)


mycursor.execute("SELECT grade FROM exam WHERE course = 'physics'")
myresult = mycursor.fetchall()

for x in myresult:
    x = int(x[0])
    sm = x + sm
    koko += 1
    
    
    
avg = sm / koko
sm = 0
koko = 0
print('phyisics average is ')
print(avg)




mycursor.execute("SELECT grade FROM exam WHERE course = 'chemistry'")
myresult = mycursor.fetchall()

for x in myresult:
    x = int(x[0])
    sm = x + sm
    koko += 1
    
    
    
avg = sm / koko
sm = 0
koko = 0
print('chemistry average is ')
print(avg)




