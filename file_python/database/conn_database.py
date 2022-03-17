import pyodbc 
#sql server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DOQB38B;'
                      'Database=ciao;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
number = 1234
name = "GeeksforGeeks"
cursor.execute("insert into dbo.Table_1(ciao) values (?)", sudoku1)


# ~ conn.commit()
conn.commit()

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.table_1')





for i in cursor:
    print(i)

###CARTELLA==database
