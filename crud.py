import sys
import pyodbc


# Configure database connection
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
    with cursor.execute(tsql,'Jake','United States'):
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
    print ('Updating Location for Nikita')
    tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
    with cursor.execute(tsql,'Sao Paulo','Nikita'):
        print ('Successfully Updated!')

# Delete
def delete():
    print ('Deleting user Nikita')
    tsql = "DELETE FROM Employees WHERE Name = ?"
    with cursor.execute(tsql,'Nikita'):
        print ('Successfully Deleted!')

if __name__ == '__main__':
    # sys.argv[0] = current file
    # sys.argv[1] = function name
    # sys.argv[2:] = function args : (*unpacked)
    # globals()[sys.argv[1]](*sys.argv[2:])
    globals()[sys.argv[1]]()