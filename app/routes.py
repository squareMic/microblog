from flask import render_template
from app import app

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