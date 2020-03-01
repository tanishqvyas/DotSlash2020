from flask_wtf import FlaskForm
from wtforms import StringField

class VideoInputForm(FlaskForm):
	username = StringField('Username')
