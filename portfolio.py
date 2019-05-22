
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('helloworld.html')

@app.route('/projects')
def projects():
    my_projects = ['Ninja Gold', 'Great Number Game', 'Disappearing Ninjas', 'Dojo Survey']
    return render_template('projects.html', projects=my_projects)


@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True)
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)
