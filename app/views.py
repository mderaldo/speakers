from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	user = {'name': 'Speaker'}
	title = 'Home'
	return render_template('index.html', title=title, user=user)