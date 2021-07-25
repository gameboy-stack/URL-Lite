import sqlite3
import random
import string
import hashlib


# ''.join([random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(size)]) 

# '''CREATE TABLE urlused(rand6d varchar(10))'''
 
# '''CREATE TABLE urlstuff(rand6d varchar(10),url varchar(5000))'''

def CheckRand6d(Arr):
    flag = True
    while(flag):
        NewRand6d = str(''.join([random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(6)]))
        if(NewRand6d not in Arr):
            flag = False
            return NewRand6d

def URLtoRand6d(givenURL,dbURLUsed,dbURLnStuff):
    cursorForUsed = dbURLUsed.cursor()
    cursorForUsed.execute(''' select * from urlused''')
    urls = cursorForUsed.fetchall()
    URLusedList = [str(i[0]) for i in urls]
    CurrRand6d = str(CheckRand6d(URLusedList))
    cursorForUsed.execute(''' insert into urlused values(?) ''',[CurrRand6d])
    dbURLUsed.commit()
    dbURLUsed.close()
    URLnStuffCursor = dbURLnStuff.cursor()
    URLnStuffCursor.execute(''' insert into urlstuff values(?,?)  ''',(CurrRand6d,givenURL))
    dbURLnStuff.commit()
    dbURLnStuff.close()
    return CurrRand6d
    
