import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hiyarI10",
    database="task"
)

mycursor = mydb.cursor()

sql = "DROP TABLE exam"

mycursor.execute(sql)