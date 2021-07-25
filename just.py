import sqlite3

# dbURLUsed = sqlite3.connect("urlUsed.db") 
# dbURLnStuff = sqlite3.connect("urlStuff.db")

# URLUsedCursor = dbURLUsed.cursor()

# URLUsedCursor.execute('''CREATE TABLE urlused(rand6d varchar(10))''')

# dbURLUsed.commit()

# dbURLUsed.close()

# URLnStuffCursor = dbURLnStuff.cursor()

# URLnStuffCursor.execute('''CREATE TABLE urlstuff(rand6d varchar(10),url varchar(5000))''')

# dbURLnStuff.commit()

# dbURLnStuff.close()

# dbURLUsed = sqlite3.connect("urlUsed.db") 
# CurrRand6d ="46"
# cursorForUsed = dbURLUsed.cursor()
# cursorForUsed.execute(''' insert into urlused(rand6d) values(?) ''',[CurrRand6d])
# dbURLUsed.commit()
# cursorForUsed.execute(''' select rand6d from urlused''')
# urls = cursorForUsed.fetchall()
# URLusedList = [str(i[0]) for i in urls]
# print(URLusedList)