#install mysql on pc
#pip install mysql (in shell)
#pip install mysql-connector or pip install mysql-connector-python (whichever works)


import mysql.connector

dataBase = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     password = 'pavlesto02'
)


#prepare a cursor object


cursorObject = dataBase.cursor()

#Creation of database

cursorObject.execute("CREATE DATABASE pavleco")

print("Database created!!")
#soo i had to install mysql-connector-python because i kept getting error even though it succesfully installed it the first way
#i could not run my code for creating database.!!
