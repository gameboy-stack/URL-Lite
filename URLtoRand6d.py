import sqlite3
import random
import string
import hashlib

def CheckRand6d(Arr):
    flag = True
    while(flag):
        NewRand6d = str(''.join([random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(6)]))
        if(NewRand6d not in Arr):
            flag = False
            return NewRand6d

def URLtoRand6d(givenURL,dbURLUsed,dbURLnStuff):
    cursorForUsed = dbURLUsed.cursor()
    cursorForUsed.execute('''query for db 1 ''')
    urls = cursorForUsed.fetchall()
    URLusedList = [str(i[0]) for i in urls]
    CurrRand6d = str(CheckRand6d(URLusedList))
    cursorForUsed.execute('''query for db 1''')
    dbURLUsed.commit()
    dbURLUsed.close()
    URLnStuffCursor = dbURLnStuff.cursor()
    URLnStuffCursor.execute(''' query for db2  ''')
    dbURLnStuff.commit()
    dbURLnStuff.close()
    return CurrRand6d
    
