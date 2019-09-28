import pyodbc

server = 'localhost'
database = 'testDB'
username = 'SA'
password = 'giorgio$1'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print('Inserting a new row into table')
tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
with cursor.execute(tsql,'Jake','United States'):
    print('Successfully Inserted!')
