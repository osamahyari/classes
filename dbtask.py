import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="hiyarI10",
    database="task"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE exam (id INT AUTO_INCREMENT PRIMARY KEY, student VARCHAR(255), course VARCHAR(255), date VARCHAR(255), grade INTEGER(255))")