from app import app 
from flask import render_template

import forms

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about', methods = ['GET', 'POST'])
def about():
    form = forms.AddTask()
    if form.validate_on_submit():
        print("Form submitted with title :", form.title.data)
        return render_template('about.html', form=form, title = form.title.data)
    return render_template('about.html', form = form)
