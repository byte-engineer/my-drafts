# Draft\Librarys\SQLite.py

# SQLite
#|> Database Is A Place Where We Can Store Data
#|> Database organized into tables.
#|> Tables Has Columns (ID, Username, Password)
#|> SQL Stand For (Structured Query Language)
#|> SQLite => Can Run in Memory or in A Single File
#|> You Can Browse File With https://sqlitebrowser.org/
#|> Data Inside Database Has Types (Text, Integer, Date)

path = r"C:\Users\Hp\Desktop\bilal\files\Codes\Python\Draft\REQs"


import sqlite3


#|> connect() => create a data base, or connect to a prevuis one.
#|> execute() => execute a Query command.
#|> close()   => close the data base.

# create and connect to a data base.
db = sqlite3.connect(path + r"\app0.db")

# Create a table.
db.execute("CREATE TABLE if not exists `users` ( ID integre, name text, prograss integre)")

# Close data base.
db.close()

#|> cursor()  # A way to execute multiple Query commends.
#|> commit()  # To save all changes.

db = sqlite3.connect(path + r"\app0.db")

# Create a cursor
cr = db.cursor()

# Execute Query commends with cursor
cr.execute("insert into users(ID, name) values(1, 'bilal')")


db.commit()



