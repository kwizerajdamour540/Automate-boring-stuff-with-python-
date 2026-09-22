import sqlite3
obj1=sqlite3.connect('dmgfreind.db',isolation_level=None)
print("this is count row in dmgfreind table:\n")
print(obj1.execute('SELECT COUNT(*) FROM DAMURU_FREIND').fetchall())
print("maximum age:")
print(obj1.execute('SELECT MAX(AGE) FROM DAMURU_FREIND').fetchall())
print("minimum age:\n")
print(obj1.execute('SELECT MIN(AGE) FROM DAMURU_FREIND').fetchall())
print("sum of age of DAMURU_FRIEND:\n")
print(obj1.execute('SELECT SUM(AGE) FROM DAMURU_FREIND').fetchall())
print("AVERAGE AGE Of DAMURU_FRIEND:")
print(obj1.execute('SELECT AVG(AGE) FROM DAMURU_FREIND').fetchall())

print("LET'S PRINT WHOLE TABLE ORDER BY AGE:\n")
for row in obj1.execute('SELECT DISTINCT * FROM DAMURU_FREIND ORDER BY AGE ASC'):
	print(row)
print("\n")

print("all name contain %IG%:")
print(obj1.execute('SELECT DISTINCT * FROM DAMURU_FREIND WHERE FIRST_NAME OR LAST_NAME LIKE "%IG%" ').fetchall())

#we gonna update phone number
obj1.execute('UPDATE DAMURU_FREIND SET PHONE="0790354308" WHERE FIRST_NAME="Patrick" ')
print("updated phone number:\n")
print(obj1.execute('SELECT DISTINCT * FROM DAMURU_FREIND ').fetchall())