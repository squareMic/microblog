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
    return render_template('index.html', title='Home', user=user)