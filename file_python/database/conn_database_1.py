import pyodbc 

import numpy as np
a=[2,3,4]
b=[3,3,4]
c=[4,3,4]

sudoku = np.array([a,b,c])
	# ~ print(a)
sudoku1=str(sudoku)
print(type(sudoku1))
import pyodbc 
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

# ~ cursor = conn.cursor()
# ~ cursor.execute('SELECT * FROM dbo.table_1')





# ~ for i in cursor:
    # ~ print(i)

###CARTELLA==database
