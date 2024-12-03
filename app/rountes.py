from flask import render_template
from app import app
# home page
@app.route('/')
def home():
    return render_template('home.html')

#The about page
@app.route('/aboutUs')
def about():
    return render_template('about-us.html')
#Projects page
@app.route('/services')
def services():
    return render_template('services.html')
#Skills page
@app.route('/portfolio')
def port():
    return render_template('portfolio.html')
@app.route('/hireMe')
def hireMe():
    return render_template('hire-me.html')
