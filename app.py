from flask import Flask ,redirect ,render_template ,request
from datetime import date
from form import ShortURLForm
from URLtoRand6d import *
import sqlite3
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env_sample')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("secret_key")

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/',methods=['POST','GET'])
def index():
    form = ShortURLForm()

    if request.method == "POST":
        givenURL_ = form.URLinput.data  

        dbURLUsed = "database_connection1"
        dbURLnStuff = "database_connection2" 

        rand6durl = URLtoRand6d(givenURL_,dbURLUsed,dbURLnStuff)
        hostURL = request.url_root
        URLLite = str(hostURL) + str(rand6durl)
        return render_template("index.html", form=form, year=date.today().year, URLLite=URLLite)

    return render_template("index.html", form=form, year = date.today().year)

@app.route('/<URLLite>')
def gURLLite(URLLite):
    dbURLUsed = "database_connection1"
    dbURLnStuff = "database_connection2" 
    
    cursorForUsed = dbURLUsed.cursor()
    cursorForUsed.execute('''query for database1''')
    urls = cursorForUsed.fetchall()
    URLusedList = [str(i[0]) for i in urls]
    dbURLUsed.close()

    if str(URLLite) in URLusedList:
        cursorForURLnStuff = dbURLnStuff.cursor()
        cursorForURLnStuff.execute('''query for database 2''' )
        reDirectURL = cursorForURLnStuff.fetchall() 
        return redirect(str(reDirectURL[0][0]))
    return render_template("error.html", year = date.today().year),404

