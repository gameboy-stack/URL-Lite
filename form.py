from wtforms import TextField
from flask_wtf import FlaskForm 


class ShortURLForm(FlaskForm):
    URLinput = TextField()



