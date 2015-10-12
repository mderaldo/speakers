from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	user = {'name': 'Speaker'}
	title = 'Home'
	return render_template('index.html', title=title, user=user)


@app.route('/profile')
def profile():
	user = {'name': 'Speaker'}
	title = 'Home'
	talks = [
		{ 
            'name': 'Talk 1', 
            'description': 'Beautiful day in Portland!', 
            'duration': '10'
        },
        { 
            'name': 'Talk 2', 
            'description': 'The Avengers movie was so cool!', 
            'duration': '10'
        }
	]
	return render_template('profile.html', title=title, user=user, talks=talks)