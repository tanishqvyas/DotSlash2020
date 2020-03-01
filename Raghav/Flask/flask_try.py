# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask, render_template
from  forms import VideoInputForm

# Flask constructor takes the name of 
# current module (__name__) as argument. 
app = Flask(__name__) 

app.config['SECRET_KEY'] = 'ff07db6c063c2f59f8aee8de6c9eadef'
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
#routes are what we type on the browser
# ‘/’ URL is bound with hello_world() function. 
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/videoinput')
def videoinput():
	form  = VideoInputForm()
	return render_template('videoinput.py', title = 'Video Input', form = form)

# main driver function 
if __name__ == '__main__': 

	# run() method of Flask class runs the application 
	# on the local development server. 
	app.run(debug  = True) 
