import sqlite3
obj1=sqlite3.connect('database1.db',isolation_level=None)
obj1.execute('CREATE TAbLE IF NOT EXISTS cat(name TEXT NOT NULL, birtdate TEXT,fur TEXT,weigth_kg REAL)STRICT')
print("let's check status of table we created:\n")
print(obj1.execute('SELECT * FROM cat').fetchall())
print("for sure nothing returned!!")
#now we gonna add some information in our database table
obj1.execute('INSERT INTO cat VALUES  ("Zophie", "2021-01-24", "black", 5.6)')
print(" LET'S ADD SOMETHING \nOUR TABLE STATUS:\n")
print(obj1.execute('SELECT * FROM cat').fetchall())
print("now you can update my table your self using input :\n")
#i'm gonna restrict hackers by using ?
n=input("enter cat name:")
b=input("enter catbirtdate:")
f=input("enter cat color:")
w=float(input("don't worrry about floating point enter cat weigth in kg :"))
obj1.execute('INSERT INTO cat VALUES(?,?,?,?)',[n,b,f,w])
print("we added those in table:\n")
obj2 = "SELECT * FROM cat WHERE name = ?"
print(obj1.execute(obj2, (n,)).fetchall())
