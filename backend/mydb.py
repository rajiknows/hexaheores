
import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'hexaheroes123',

)
#creating the cursor object 
cursorObject = dataBase.cursor()


#create the database
cursorObject.execute("CREATE DATABASE persona ")

print("database created")

