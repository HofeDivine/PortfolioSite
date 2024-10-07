from flask import render_template
from app import app
# home page
@app.route('/')
def home():
    return render_template('home.html')

#The about page
@app.route('/about')
def about():
    return render_template('about.')
#Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')
#Skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')
