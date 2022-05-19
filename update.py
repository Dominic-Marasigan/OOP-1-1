import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
                                r'DBQ=C:\Users\lenovo\Documents\Database1.accdb;')
    print("Database is Connected")

    user_id = 3
    Address = "Cavite"
    database = connection.cursor()
    database.execute('UPDATE Table1 SET Address=? WHERE id=?',(Address,user_id))

    user_id = 10
    Fullname = "Dominic Z. Marasigan"
    Grade = "97"
    database = connection.cursor()
    database.execute('UPDATE Table1 SET Fullname=? WHERE id=?', (Fullname, user_id))
    database.execute('UPDATE Table1 SET Grade=? WHERE id=?', (Grade, user_id))
    connection.commit()

    print("Database is updated")

except pyodbc.Error:
    print("Database is NOT updated")