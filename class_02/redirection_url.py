import time 
from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return f'<h1>welcome to home page</h1>'


@app.route('/pass')
def passed():
    return f'<h1>congruation you have passed</h1>'


@app.route('/fail')
def failed():
    return f'<h1>sorry you have failed</h1>'

@app.route('/score/<name>/<int:num>')
def score(name,num):
    if num>30:
        return redirect(url_for('passed'))
    else:
        return redirect(url_for('failed'))


if __name__=='__main__':
    app.run(debug=True)