from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
# def index():
#     return "Hello, World!"
def index():
    user = {'username': 'squaremic'}
#     return '''
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!</h1>
#     </body>
# </html>'''
    posts = [
        {
            'author': {'username': 'John'},
            'body': {'Beautiful day in Portland!'}
        },
        {
            'author': {'username': 'Susan'},
            'body': {'The Avengers movie was so cool!'}
        },
        {
            'author': {'username': 'squaremic'},
            'body': {'This blog kiks a**!'}
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
