import sqlite3
i=1
print("now we gonna loop database1 content ")
obj1=sqlite3.connect('database1.db',isolation_level=None)
for row in obj1.execute('SELECT * FROM cat'):
	print(f"row[{i}]:{row}")
	i+=1
print("in above long list let's retrieve black and brown cat only:")
print(obj1.execute('SELECT * FROM cat WHERE fur=="black" OR fur=="brown"').fetchall())