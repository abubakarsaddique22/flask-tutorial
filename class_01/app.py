from flask import Flask

app =Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>wellcome to home page</h1>'

@app.route('/about')
def about():
    return '<h1>welcome to about page</h1>'


@app.route('/welcome/<name>')
def welcome(name):
    return f'<h1>Hi {name},you are welcome in this page</h1>'


@app.route('/addition/<int:num>')
def addition(num):
    return f'<h1>input is this {num} and output is this after added 10 + {num} = {10+num}</h1>'


@app.route('/addition_two_number/<int:num1>/<int:num2>')
def addition_two_number(num1,num2):
    return f'<h1>input is this {num1,num2} and output is this {num1+num2}</h1>'

if __name__ =='__main__':
   app.run(debug=True)