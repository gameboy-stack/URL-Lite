from flask import Flask ,redirect ,render_template ,request
from datetime import date
from form import ShortURLForm
from URLtoRand6d import *
import sqlite3
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")

# ''.join([random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(size)]) 

# '''CREATE TABLE urlused(rand6d varchar(10))'''
 
# '''CREATE TABLE urlstuff(rand6d varchar(10),url varchar(5000))'''

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/',methods=['POST','GET'])
def index():
    form = ShortURLForm()

    if request.method == "POST":
        givenURL_ = form.URLinput.data  

        dbURLUsed = sqlite3.connect("urlUsed.db") 
        dbURLnStuff = sqlite3.connect("urlStuff.db") 

        rand6durl = URLtoRand6d(givenURL_,dbURLUsed,dbURLnStuff)
        hostURL = request.url_root
        dwarfurl = str(hostURL) + str(rand6durl)
        return render_template("index.html", form=form, year=date.today().year, dwarfurl=dwarfurl)

    return render_template("index.html", form=form, year = date.today().year)

@app.route('/<getDwarfURL>')
def gdURL(getDwarfURL):
    dbURLUsed = sqlite3.connect("urlUsed.db") 
    dbURLnStuff = sqlite3.connect("urlStuff.db")
    
    cursorForUsed = dbURLUsed.cursor()
    cursorForUsed.execute(''' select * from urlused ''')
    urls = cursorForUsed.fetchall()
    URLusedList = [str(i[0]) for i in urls]
    dbURLUsed.close()

    if str(getDwarfURL) in URLusedList:
        cursorForURLnStuff = dbURLnStuff.cursor()
        cursorForURLnStuff.execute(''' select url from urlstuff where rand6d = "''' + getDwarfURL +'''"''' )
        reDirectURL = cursorForURLnStuff.fetchall() 
        return redirect(str(reDirectURL[0][0]))
    return render_template("error.html", year = date.today().year),404

if __name__ == "__main__":
    app.run(debug=True,port=8080)