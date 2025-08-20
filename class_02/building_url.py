import time 
from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return f'<h1>welcome to home page</h1>'


@app.route('/pass/<sname>/<int:marks>')
def passed(sname, marks):
    return f'<h1>Congratulation {sname}, you achieved marks = {marks}. You have passed!</h1>'

@app.route('/fail/<sname>/<int:marks>')
def failed(sname, marks):
    return f'<h1>Sorry {sname}, you achieved marks = {marks}. You have failed!</h1>'


@app.route('/score/<name>/<int:num>')
def score(name,num):
    if num>30:
        return redirect(url_for('passed',sname=name,marks=num))
    else:
        return redirect(url_for('failed',sname=name,marks=num))


if __name__=='__main__':
    app.run(debug=True)