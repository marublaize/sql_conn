import sys
import pyodbc
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__main__)
app.debug = True


# Database connection
server = 'tcp:localhost'
database = 'EmployeesDB'
username = 'sa'
password = 'P@ssw0rd123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Create
def create():
    print ('Inserting a new row into table')
    tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
    with cursor.execute(tsql,'Kathuann Deniz','Sao Paulo'):
        print ('Successfully Inserted!')

# Read
def read():
    print ('Reading data from table')
    tsql = "SELECT Name, Location FROM Employees;"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()

# Update
def update():
    print ('Updating Location for Pedro Moreira')
    tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
    with cursor.execute(tsql,'Macae','Pedro Moreira'):
        print ('Successfully Updated!')

# Delete
def delete():
    print ('Deleting user Tom')
    tsql = "DELETE FROM Employees WHERE Name = ?"
    with cursor.execute(tsql,'Tom'):
        print ('Successfully Deleted!')

if __name__ == '__main__':
    globals()[sys.argv[1]]()