import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
                                r'DBQ=C:\Users\lenovo\Documents\Database1.accdb;')
    print("Database is Connected")

    database = connection.cursor()
    mydata = (

        (10, "Dominic Z. Marasigan", 19, "Cavite", "BS CPE", 97),
        
    )

    database.executemany('INSERT INTO Table1 VALUES (?,?,?,?,?,?)', mydata)
    connection.commit()
    #print(x)

    print("Data is inserted")

except pyodbc.Error:
    print("Data is NOT inserted", e)